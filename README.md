# codelijsten Uitwisselingsplatform

IN PROGRESS: de codelijsten zijn nog niet in gebruik.

Deze repository omvat een aantal codelijsten voor het uitwisselingsplatform https://data.uitwisselingsplatform.be.

Per codelijst wordt een subdirectory aangemaakt. Elke codelijst is een of meerdere RDF files in de turtle syntax volgens het [SKOS vocabularium](https://www.w3.org/TR/skos-primer/).

# vormafspraken de codelijsten


- eigenschappen te gebruiken met conceptschemes:

|eigenschap | nota |
|-----------|------|
skos:prefLabel | een unieke naam voor het conceptscheme
skos:definition | een definitie van de codelijst

- eigenschappen te gebruiken met concepts:

|eigenschap | nota |
|-----------|------|
skos:prefLabel | een unieke naam voor het concept
skos:definition | een definitie van het concept
skos:inscheme  | het conceptscheme waartoe dit concept behoort
skos:topConceptOf | het conceptscheme waarvan dit concept een top concept is 
skos:narrower | de concepten die onder dit concept hangen in de conceptscheme boom.

- gebruik language-tagged strings i.p.v. plain literals
Dus `"mijn label@nl` i.p.v. `"mijn label"`

- We verwachten een hierarchie in 1 richting. Het is voldoende om de hierarchie in 1 richting uit te drukken. Het is aan de afnemers om indien voor hen nodig ook de omgekeerde relatie te berekenen. Dat maakt de data ook overzichtelijk. 



