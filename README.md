# ProgettoTesiEmotionClassification
Il sistema hardware realizzato è basato su sensori biometrici e microcontrollori Arduino che
permette la raccolta di dati degli utenti per una successiva interpretazione e classificazione del
loro stato emotivo. A tal proposito, un valido strumento di supporto è sicuramente l’uso di
algoritmi di machine learning, cioè strumenti che simulano la capacità del cervello umano di
apprendere e generalizzare le informazioni. In particolare, nel presente lavoro sono stati
utilizzati metodi del deep learning. Questi ultimi si presentano come una evoluzione di quelli
del machine learning capaci di trattare dati di grande cardinalità e complessità. Per quanto
riguarda il sistema hardware l’idea è stata quella di realizzare un guanto formato da
microcontrollori e sensori Arduino quanto più leggeri possibile. Per evitare il problema
dell’utilizzo dei fili introdotto precedentemente, per il rilevamento dei dati è stata utilizzata una
trasmissione Wi-Fi ed è stato adottato un sistema client-server. Questi ultimi sono stati
memorizzati in un data storage lato server su cui è stata applicata la classificazione. Infine, per
gestire il problema dell’autonomia del sistema è stata utilizzata una batteria portatile. Uno
studio iniziale ha permesso di determinare quali fossero i parametri fisiologici e
comportamentali più comunemente misurati in lavori simili. Si è scelto pertanto di misurare la
frequenza cardiaca attraverso il modulo KY-039, l’EDA attraverso il sensore DHT11, i movimenti del corpo attraverso il modulo GY-521 e il tono della voce attraverso il modulo KY037. Tutti i sensori utilizzati sono gestiti da una pila di 4 microcontrollori Arduino Nano. Come accennato precedentemente per l’acquisizione dei dati si è fatto uso di un’architettura clientserver. In questo contesto un client è rappresentato da un Modulo Wi-Fi ESP8266 che invia i
dati ricevuti dai sensori ad un server sviluppato in Java che riceve i dati e li analizza. Le misure
sono state acquisite durante un processo di stimolazione delle emozioni, realizzato mostrando
ai partecipanti coinvolti nell’esperimento alcune immagini selezionate tra quelle del dataset
International Affective Picture System o IAPS. Dunque, è stato scelto dalle
immagini IAPS un sottoinsieme di immagini secondo le emozioni principali, cioè: felicità,
rabbia, tristezza e paura. Tali immagini sono state mostrate ad un gruppo di studenti iscritti al
Corso di Laurea in Informatica presso l’Università Degli Studi di Salerno, con un’età compresa
tra i 22 e i 25 anni, che hanno guardato le immagini fornendo un feedback in tempo reale. Per
una corretta realizzazione del dataset è stato necessario effettuare una sincronizzazione
temporale dei dati. Infine, è stata effettuata l’analisi dei dati e la classificazione: quindi si è fatto
uso di tecniche di deep learning e si è deciso di utilizzare la rete neurale MLP (il codice python utilizzato è disponibile nella repository).
