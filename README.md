# projekta_darbs

Projekta uzdevums:

  Mūsdienās meklējot jaunas preces, bieži vien rodas problēma ar preču klāstu un to parametriem. Klients vienmēr vēlas vislabāko un par vislētāko cenu, tāpēc esmu izstrādājis programmu, kas, šajā gadījumā, no mājaslapas "https://www.1a.lv", ar lietotāja iesaisti, atrod vēlamās preces un to parametrus un apkopo tās pārredzamā veidā excel failā, kā arī atrod vislabākās preces un aprēķina to kopsummu.
  
  Kodu palaižot, lietotājam jāievada meklēto preču skaits un pašas preces (3 preces - pašlaik tās ir tikai videokarte, cietais disks un procesors). Tad tiek atvērts "https://www.1a.lv", meklētājā tiek ierakstīta pirmā prece un tiek atvērta meklēšanas rezultātu lapa. Tad tiek nolasīti trīs populārāko preču parametri (piem., cietā diska ietilpība, lasīšanas ātrums un rakstīšanas ātrums), nosaukumi un cenas, saglabājot tos CSV failā (lai nepazaudētu informāciju un būtu vieglāk rakstīt kodu pa daļām). Procesu atkārto visām lietotāja ievadītajām precēm. Tiek izveidots Excel fails ar lapām, kas attiecināmas uz meklētajām precēm. No CSV failiem tiek nolasīta attiecīgā informācija un tā tiek apstrādāta, ja nepieciešams (piem., 1 TR pārveido uz 1024 GB). Tad šī informācija tiek saglabāta sarakstā, lai procesu varētu atkārtot visām top precēm. No saraksta tā tiek pārvietota uz attiecīgajām Excel lapām un šūnām. No katras Excel lapas jeb no katra preču top trīs tiek atrasta visveiktspējīgākā/ietilpīgākā prece (piem., cietais disks tiek salīdzināts pēc prioritātes [ietilpība -> lasīšanas ātrums -> rakstīšanas ātrums -> cena], ja pirmais parametrs ir vienāds ar otro, tad tiek salīdzināti nākamie) un to ieraksta rezultātu lapā. Visbeidzot tiek nolasītas cenas un tiek aprēķināta to summa, kas tiek izvadīta zem visveiktspējīgākajām/ietilpīgākajām precēm.

Izmantotās bibliotēkas:

  + Selenium biblieotēka - tiks izmantota, lai ievadītu "https://www.1a.lv" meklētājā preces, kuras nepieciešams atrast;
  + Beautiful Soup bibliotēka - tiks izmantota tīmekļa skrāpēšanai, jeb lai atrastu "https://www.1a.lv" norādītos preču parametrus, nosaukumus un cenas;
  + Python iebūvētās bibliotēkas time funkciju - tiks izmantots, lai norādītu koda izpildes gaidīšanas laiku pirms vai pēc norāžu izpildes;
  + Openpyxl bibliotēka - tiks izmantota darbībām Excel, lai izveidotu Excel failu
  + Modulis re - tiks izmantots, lai CSV failos atrastu nepieciešamo informāciju (šajā gadījumā - skaitliskās vērtības)

P.S. Augšuplādētie faili, kas saglabāti ar "faila_nosaukums_0", ir izveidoti ar kodu. Tie ir izveidoti, lai, ja nepieciešams pārbaudīt kodu, to var palaist neko nemainot.
