# **OTConverter**

Sovellus on valuutanvaihtolaskuri. Se käyttää [exhangerate.host](https://exchangerate.host/#/) API:tä selvittääkseen valuuttakurssit reaaliajassa. Sovelluksessa on 170 eri maan valuuttaa sekä Bitcoin.



## Miten sovellus toimii?

Asenna poetry:
```bash
poetry install
```

Käynnistä sovellus:
```bash
poetry run invoke start
```

Valitse mistä valuutasta haluat vaihtaa:
```bash
Convert from: EUR
```

Valitse vaihdettava määrä:
```bash
Amount: 10
```

Valitse mihin valuuttaan haluat vaihtaa:
```bash
Convert to: USD
```

Ja sovellus antaa sinulle vastauksen!
```bash
10 EUR = 11.8848 USD as of 12.04.2021
```


### Sovelluksen testaus

```bash
poetry run invoke test
```


### Sovelluksen testikattavuus

```bash
poetry run invoke coverage-report
```


### Linkit työhön:

* [Linkki vaativuusmäärittelyyn](https://github.com/Sanexi/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
* [Linkki työaikakirjanpitoon](https://github.com/Sanexi/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)


