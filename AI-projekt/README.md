### TeddyAI- En AI som vet vad du behöver för att hålla humöret uppe!

# Innehåll:
  * [Projektbeskrivning](#Projektbeskrivning)
    * [Frågeställning](#Frågeställning)
    * [Begränsningar](#utförande)
  * [Lite Hjälp](#hjälp)
  * [Filer](#filer)
  * [Installationer](#installationer)
---

# Projektbeskrivning
Projekt där AI används för ansiktsigenkänning och känsloidentifiering.

## Frågeställning
Jag vill se om jag kan göra en AI som känner igen ens ansikte och identifierar ett allmänt känslotillstånd, så som glad/ledsen och sedan rekommendera lämpligt internet-innehåll. 

*Exempel*: AI:n anser att jag inte är glad och rekommenderar därför en gullig kattvideo eller ger en länk till [eyebleach](https://reddit.com/r/eyebleach) på reddit.

## Begränsningar
För att det här projektet ska kunna bli någorlunda klart har jag valt att begränsa min "*humörvidd*". Detta innebär att min AI kommer att klassificera en person som *glad* eller *inte glad*. Eftersom humörvidden är så begränsad och vinklad mot glädje/inte glädje kommer det finnas fler ledsna personer än glada personer enligt AI:n, vilket kan vara lite sorgligt. För att motverka det här kan man se till att le lite extra för kameran!


# Hjälp
* För att lära mig hur man får ansiktsigenkänning att fungera i **python** följde jag [denna](https://towardsdatascience.com/real-time-face-recognition-an-end-to-end-project-b738bb0f7348 "Real-Time Face Recognition: An End-To-End Project") guide av [Marcelo Rovai](https://medium.com/@rovai). Han använder en Raspberry Pi med kamera, men jag använder min skoldator och tillhörande webcam.

# Filer

# Installationer
Följande behövs installeras innan start:
* OpenCV-python `pip install opencv-python` och `pip install --user opencv-contrib-python` (se till att OpenCV inte redan är installerat).
  
* Se till att pillow är installerat, om inte kan man använda `pip install pillow`.
