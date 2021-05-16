# **OTConverter**

Sovellus on valuutanvaihtolaskuri. Se käyttää [exhangerate.host](https://exchangerate.host/#/) API:tä selvittääkseen valuuttakurssit reaaliajassa. Sovelluksessa on 170 eri maan valuuttaa sekä Bitcoin.

Sovellus on tehty Helsingin yliopiston Ohjelmistotekniikan kurssille harjoitustyönä.


## Linkit työhön:

* [Vaativuusmäärittelyyn](https://github.com/Sanexi/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
* [Käyttöohjeisiin](https://github.com/Sanexi/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)
* [Releaseen](https://github.com/Sanexi/ot-harjoitustyo/releases)
* [Arkkitehtuuriin](https://github.com/Sanexi/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)
* [Testaukseen](https://github.com/Sanexi/ot-harjoitustyo/blob/master/dokumentaatio/testaus.md)
* [Työaikakirjanpitoon](https://github.com/Sanexi/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)




## Miten sovellus toimii?

Asenna riippuvuudet:
```bash
poetry install
```

Käynnistä sovellus:
```bash
poetry run invoke start
```

### Sovelluksen testaus

```bash
poetry run invoke test
```


### Sovelluksen testikattavuus

```bash
poetry run invoke coverage-report
```


### Pylint-tarkastelu

```bash
poetry run invoke lint
```


#### Projektin Python versio: 3.6
