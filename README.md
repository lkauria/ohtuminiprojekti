# Ohtuminiprojekti!

![GHA workflow badge](https://github.com/jyrikangas/ohtuminiprojekti/workflows/CI/badge.svg)

# Linkit 

- [testikattavuus](https://app.codecov.io/gh/jyrikangas/ohtuminiprojekti)
- [Tästä](https://helsinkifi-my.sharepoint.com/:x:/g/personal/kajy_ad_helsinki_fi/Ef1LbjVAhbtOkqyw6ePnJrQBQsuSYnmgXV5_LpB7lgaqeA?e=40hfPr) backlogeihin. Välilehdellä 1 product backlog, välilehdellä 2 sprint backlog ja sprintin burndown -käyrä.

- [Linkki appiin](https://ohtuminiappli2.fly.dev:5000/)
# Definition of done

- Toiminnallisuus toteutettu
- asiakkaan käytettävissä
- dokumentoitu
- testattu kattavasti

# Ohjelman käyttö

  1. Kopioi repositorio omalle koneellesi
  2. Asenna riippuvuudet komennolla:
  ```bash
  poetry install
  ``` 
  4. Siirry kansioon src
  5. Aja init_db.py komennolla:
  ```bash
  python3 init_db.py
  ```
  3. Siirry virtuaaliympäristöön komennolla:
  ```bash
  poetry shell
  ```
  4. Käynnistä sovellus komennolla:
  ```bash
  flask run
  ```
        
