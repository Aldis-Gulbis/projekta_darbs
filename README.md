# projekta_darbs

Projekta uzdevums:
  Mūsdienās meklējot jaunas preces, bieži vien rodas problēma ar preču klāstu un to parametriem. Klients vienmēr vēlas vislabāko un par vislētāko cenu, tāpēc esmu izstrādājis programmu, kas, šajā gadījumā, no mājaslapas "https://www.1a.lv" atrod vēlamās preces un to parametrus un apkopo tās pārredzamā veidā excel failā, kā arī atrod vislabākās preces un aprēķina to kopsummu.
  Šajā projekta darbā tiks meklētas noteiktas datora komponentes (cietais disks, videokarte, procesors), ko ierakstīs pats lietotājs. 1a.lv meklētājā tiks ievadīti šo preču nosaukumi un no trim vai vairāk populārākajām precēm (ko arī ievada pats lietotājs) tiks nolasīta nepieciešamā informācija - parametri (piem., ietilpība, lasīšanas ātrums utt.), cenas un nosaukumi - un tiks saglabāta CSV failos (lai nepazaudētu informāciju un būtu vieglāk rakstīt pašu kodu). Tad informācija tiek nolasīta no CSV failiem, apstrādāta un attiecīgi ievietota Excel failā. Lai tiktu pie gala rezultāta Excel esošā informācija tiek nolasīta un tiek atrasts labākā un lētākā prece (piem., cietais disks tiek salīdzināts pēc šādas prioritātes [ietilpība -> lasīšanas ātrums -> rakstīšanas ātrums -> cena], ja sakrīt pirmais parametrs, tad tiek salīdzināts nākamais). Pēc tam tā tiek ievadīta rezultāta lapā un aprēķināta summa, kas būtu jāsamaksā par šīm precēm.

Izmantotās bibliotēkas:
  + Selenium biblieotēka - tiks izmantota, lai ievadītu "https://www.1a.lv" meklētājā preces, kuras nepieciešams atrast;
  + Beautiful Soup bibliotēka - tiks izmantota tīmekļa skrāpēšanai, jeb lai atrastu "https://www.1a.lv" norādītos preču parametrus, nosaukumus un cenas;
  + Python iebūvētās bibliotēkas time funkciju - tiks izmantots, lai norādītu koda izpildes gaidīšanas laiku pirms vai pēc norāžu izpildes;
  + Openpyxl bibliotēka - tiks izmantota darbībām Excel, lai izveidotu Excel failu
      - augšuplādētais fails ir izveidots izmantojot kodu, tas tiks ir saglabāts ar "rezultāts_0.xlsx", lai gadījumā, ja nepieciešams pārbaudīt kodu, to ir iespējams uzreiz palaist
  + Modulis re - tiks izmantots, lai CSV failos atrastu nepieciešamo informāciju (šajā gadījumā - skaitliskās vērtības)
