#!/bin/bash

clear
echo "
#################################################################################
#                       Script for update kibana agents                         #
#               Creator: Lukas Kopcak ERPKT-VASP_APE                            #
#               Contact: Lukas.Kopcak@telekom.com                               #
#    Before executing check paths if eveything is OK! Use on your own risk!     #
#               Version: 1.0         Last Update: 9.5.2023                      #
#################################################################################
"
#LEGENDA
#1- Premenne pouzite v scripte.
#2- Hlavna podmienka pre menu aky update chceme urobit.
#3- Podmienky pre samotny update agenta.
#4- Odosalnie na email o stave updatu.
#5- Update yml file-u
#6- sed, awk = prikazy pre vyfiltrovanie paternu a nasledne pre update noveho conf suboru

#2/1
while true; do
read -p "Spustil si script na update kibana agentov, prajes si pokracovat?  Y/N:  " decision



#1
#APM-var
apm_check="/appl/lukas/elastic_apm"

#METRIC-var
metricb="/etc/metricbeat/metricbeat.yml"

#FILEBEAT-var
SOURCE_F="/appl/lukas/elastic_sw/filebeat.yml"
TEMP_F1="/appl/lukas/elastic_sw/temp.yml"
TEMP_F2="/etc/filebeat/filebeat.yml.tmp"
DEST_F="/etc/filebeat/filebeat.yml"

#OTHERS
decision=${decision^}
email="Lukas.Kopcak@telekom.com"
host=$(hostname)
c_time=$(date +"%Y-%m-%d %H:%M:%S")


#2/2
if [ $decision == "Y" ]; then
        echo "Vyber si s cim chces zacat"


        read -p "Ak chces zacat s APM-Agentom stlac 1, METRICBeatom stlac 2 alebo FILEBeat stlac 3: " agent
                #3/1
                if [ $agent -eq 1 ]; then
                        if [ -e "$apm_check" ]; then

                                echo "Subor $apm_check existuje, zacinam s updateom"
                                set -x

                                rm -rfi $apm_check/*
                                cp /appl/lukas/elastic_sw/elastic-apm-agent-1.41.0.jar /appl/lukas/elastic_apm
                                ln -s $apm_check/elastic-apm-agent-1.41.0.jar $apm_check/apm-agent.jar
                                set +x
                                #4
                                echo "Update apm agenta bol spusteny: $c_time a prebehol uspesne na servery: $host." | mail -s "Update APM-agent" "$email"

                                echo "Update dokonceny"
                        else
                                echo "Subor $apm_check neexistuje."
                        fi
                #3/2
                elif [ $agent -eq 2 ]; then

                        echo "Kontrola ci Metricbeat je na servery..."
                        if rpm -q metricbeat; then
                                echo "Zacinam s updateom metricbeat..."
                                set -x

                                systemctl stop metricbeat.service
                                yum remove metricbeat.x86_64
                                yum install /appl/lukas/elastic_sw/metricbeat-8.6.2-x86_64.rpm
                                rm -rfi /etc/metricbeat/metricbeat.yml
                                cp /appl/lukas/elastic_sw/metricbeat.yml /etc/metricbeat/
                                set +x

                                #5
                                read -p "Zadaj tag servisu: " tag_m
                                read -p "Zadaj prostredie ewu/tua/prod : " env_m
                                        sed -i 's/\(tags:\s*\[.*\)\("voicebiometrics-server"\)\(.*\)/\1"'$tag_m'"\3/' "$metricb"
                                        sed -i 's/\(env:\s*\["\)[^"]*\(\"\]\)/\1'"$env_m"'\2/' "$metricb"


#                               systemctl start metricbeat.service
#                               systemctl status metricbeat.service
                                #4
                                echo "Update Metricbeatu bol spusteny: $c_time a prebehol uspesne na servery: $host Prostredie: $env_m. " | mail -s "Update Metricbeat" "$email"

                        else
                                echo "Metricbeat nieje na tomto servery..."
                        fi
                #3/3
                elif [ $agent -eq 3 ]; then

                        echo "Kontrola ci je Filebeat na servery..."
                        if rpm -q filebeat; then
                                echo "Zacinam s updateom Filebeat..."
                                set -x

                                systemctl stop filebeat.service
                                yum remove filebeat.x86_64
                                yum install /appl/lukas/elastic_sw/filebeat-8.6.2-x86_64.rpm
                                set +x

                                #6
                                sed -n '/filebeat.inputs:/,/# ============================== Filebeat modules ==============================/p' $SOURCE_F | sed '$d' > $TEMP_F1

                                awk -v start="# ============================== Filebeat inputs ===============================" \
                                        -v end="# ============================== Filebeat modules ==============================" \
                                        -v file="$TEMP_F1" 'BEGIN {p=1}
                                        $0 ~ start {print; p=0; while (getline < file > 0) print}
                                        $0 ~ end {p=1}
                                        p' $DEST_F > $TEMP_F2

                                set -x
                                        mv $TEMP_F2 $DEST_F
                                        rm $TEMP_F1
                                        echo "Operation completed!"



#                               systemctl start metricbeat.service
#                               systemctl status metricbeat.service
                                set +x
                                #4
                                echo "Update Filebeatu bol spusteny: $c_time a prebehol uspesne na servery: $host " | mail -s "Update Filebeat" "$email"

                        else
                                echo "Filebeat nieje na tomto servery..."
                        fi
                else
                        echo "Zadal si nespravnu hodnotu: 1=apm, 2=metric, 3=file"
                fi

else
        echo "Ukoncil si update"
        break
fi
done

