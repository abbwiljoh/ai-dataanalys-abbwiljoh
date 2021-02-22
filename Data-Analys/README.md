# Dataanalys av William Johansson

**Innehåll:**
  - [119870 Första Projektet](https://github.com/abbindustrigymnasium/ai-dataanalys-abbwiljoh/tree/main/Data-Analys/119870 "Det första och enda projektet jag hann klart med.")

## 119870-projektet
Jag döpte projektet till 119870 för att det är namnet på den fil där man kan hitta rådata för projektet. Uppgiften var som så att man skulle läsa in data från en given rådata-fil och sedan dela upp och identifiera olika sorters steg (i detta fall löpsteg och gångsteg) och sedan redovisa resultatet i en fil i csv-format.

- ##### *[_analysis.py](https://github.com/abbindustrigymnasium/ai-dataanalys-abbwiljoh/blob/main/Data-Analys/119870/119870_analysis.py "Själva Analys-filen")*
  - Analysfilen för rådatan. Koden är kommenterad för att man enklare ska förstå vad det är som händer. Något lite speciellt med mitt program är kanske att jag inte använder något tredjepartsbibliotek (som pandas eller numpy) för att hantera datan. Detta är delvis för att jag inte förstod mig på hur pandas manipulerade csv-datan, men mest för att jag ville ha full koll och kontroll över hela processen. Jag tycker också att själva processen med *moving average* och själva identifieringen av stegen. 


- ##### *[_android_formatter.py](https://github.com/abbindustrigymnasium/ai-dataanalys-abbwiljoh/blob/main/Data-Analys/119870/119870_android_formatter.py "Formaterare")*
  - När jag blev klar med projektet ville jag självklart testa med mina egna värden från min mobil. Enda problemet var att min apps format på datan var annorlunda från rådatans. Därför skapade jag ett mycket enkelt program som omvandlade appens utdata till rätt format i en ny fil. Om du själv vill testa lägga in din egen data (vilket jag kan rekommendera) kan du ladda hem [Accelerometer Analyzer](https://play.google.com/store/apps/details?id=com.lul.accelerometer "Accelerometer-appen jag använt") från Google Play Store.

- ##### *[rawdata_119870.csv](https://github.com/abbindustrigymnasium/ai-dataanalys-abbwiljoh/blob/main/Data-Analys/119870/rawdata119870.csv "Rådata")*
  - Rådata från Christer själv.
