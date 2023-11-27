# MatMa - Matematisk læringsprogram


## 1. Projektets formål og målgruppe: 

Vores app henvender sig specifikt til begyndelsen af folkeskolen i vores mening er det omkring 0-4. Faget er matematik og vi gør det på en meget simpel metode. Ligesom man ofte har gjort i dansk, så sætter man i starten eller slutningen af timen cirka 10-30 minutter af til læsning. Vores ide prøver at gøre det samme med matematik, det giver ungerne en chance for lige at komme ind i spillet og vågne fra det tidligere frikvarter. Vores endelige formål/problem er at matematik kan virke meget uoverskueligt fordi ens hjerne ikke skifter så let fra fag til fag. Derfor vil vi komme med en mulighed som kunne løse det.

## 2. Benyttede designmønstre

Vi havde misforstået hvordan design patterns fungeret, og vi fik talt med dig om det i timen d. 27 November. Vi forstod det som at f.eks. i command patternet,treode vi at man skulle bruge ```command=CreateWindow1```, til at kalde på metoder, vi havde lavede i vores class, når f.eks. en knap blev trykket på vores brugergrænseflade. 

Command patterns går ud på at vi har en class som hedder command, hvor der er en execute metode. Så der der andre class, som f.eks. addition, som nedarvler fra command classen, og bruger execute. 

Vi har brugt designmønstreret command patterns, hvor vi bruger command til at kalde på forskellige funktioner og, når en knap som for eksempel bliver trykket, skal den kalde på en specifik funktion. Et eksempel i vores kode, kan være når den skal tjekke om svaret er korrekt, kan man enten trykke på ”Tjek” knappen eller bruge ENTER tasten på ens tastatur. 
Altså når f.eks. en knap bliver trykket på, kalder den på commanden, som så gør hvad den har fået instruks til.  

## 3. Udviklingsprocessen

Inden vi startede med at lave vores program, så brainstormene vi om hvilken læringsapp vi gerne vil lave. Her fik vi ideen at vi gerne vil lave en matematisk læringsapp, som der vil kunne hjælpe skoleelever, med f.eks. deres hovedregning. 

Under udviklingsprocessen, så havde vi delt op hvem der lavede hvad. F.eks. stod Haseeb for at få lavet GUI, Mikkel stod for at lave de individuelle knapper til vores program, dette består af f.eks. addition, multiplikation, subtraktion, tjek og næste knapper. Her fik vi så koblet knapper til at blive kørt, når de bliver trykket på.  Malthe stod så for at lave matematikken bag programmet, så man vil kunne få nye matematik spørgsmål når man trykker på næste opgave. 

Under udviklingen af vores program, så støtte vi også ind på nogen udfordringer. Den del som Haseeb stod for, så som at få den til at displaye nye tal ordenligt, samt generere nye tal, til næste regnestykke. Vi havde også problemer med at displaye alle GUI elementer på hovedmenuen. Vi fik løst alle problemer vi havde og indtil videre har vi ikke fundet nogen bugs. 
Men det var ikke kun her vi havde problemer, vi havde f.eks. også problemer i forhold til matematikdelen, hvordan vi kunne tage et input og så tjekke om inputtet var lig med opstillede matematiske opgave.  Dette ville man også kunne se i commits’ne at vi fik implementeret user input, hvor den vil tjekke for svaret, men på grund af at mange af vores commits kørte ind i hinanden, så er der nogen af commitsne, som der blev lavet ikke kan ses. 

Efter user inputsne var blevet tilføjet, så blev matematikken først sat ind i sine egene classer. Senere lavede vi dem om til funktioner. Grunden til at vi prøvede at lave dem om til classer og funktioner, var fordi vi gerne vil have kørt matematikken i et loop, så man hele tiden vil få nye opgaver. Dette ledte til implementeringen af range, som kan ses i commitsne fra den 13. november 2023. Men her fandt vi ud af at det ikke virkede og vi fjerne rangen. Vi fandt så ud af at vi ikke skulle lave selve matematikken til sine egne funktioner, men at de skulle blive sat ind i addition, multiplikation, subtraktion funktionerne, hvor vi også havde fjernet rangen fra koden. Dette kan ses på commitsne fra den 15. november 2023. Efter grundelen af matematikken var blevet lavet, så tilførte vi matematikken i hele koden, sammen med GUI koden. Her har vi gjort at vores user input kommer fra den text box, hvor man kan skrive svaret ind. Her efter vil programmet kun tjekke om svaret er korrekt hvis man trykker på boksen tjek eller trykker ENTER på tastaturet, i koden hvor den tjekker, så kan man se at der bliver brugt .get() efter random_number og random_number2. Det som .get() bag random_number og random_number2 gør, er at den finder de tidligere værdiger som der blev lavet.

## 4. Vores brugergrænseflade

Vores brugergrænseflade er meget simpel, vi har en hovedmenu og 3 undervinduer, samt en hjælpe menu. 

Når man åbner programmet, møder man hovedmenuen, hvor man har fire muligheder. Addition, Subtraktion, Multiplikation og hjælp knapperne. Først starter man med at indsætte det laveste og højeste tal, man vil regne med. Efter vælger man kategorien af matematik som man har lyst til at lave. Når man er inde på f.eks. addition, får man et regnestykke givet med tal mellem ens laveste og højeste værdier, man indsatte i hovedmenuen. Når man indsætter sit gæt, kan man enten trykke ”Tjek” eller ENTER på tastaturet, for at tjekke om man har svaret korrekt. Efter kan man enten tryk næste og få et nyt regnestykke eller trykke på hovedmenuknappen, for at vende tilbage til hovedmenuen. Hvis man bliver i tvivl på nogen punkter, kan man trykke på ”Hjælp” knappen, og få en forklaring. 



![image](https://github.com/Twinbo/laerings_app/assets/142223202/c72d8737-32b9-4308-9578-48fe2bea046f)

## 5. Test skema

![image](https://github.com/Twinbo/laerings_app/assets/142223202/adc3a457-f18d-44db-8db7-b793c5d97be0)
