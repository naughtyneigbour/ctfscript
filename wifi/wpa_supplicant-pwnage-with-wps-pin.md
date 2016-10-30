#Trouver le password d'un wifi avec WPS pin et wpa_supplicant

Si on a un wps pin valide, on peut facilement retrouver le password d'un wifi avec wpa_supplicant. 

## Étapes

1. Créer un fichier de config dans le dossier courant avec le contenu comme suit :

```
ctrl_interface=/var/run/wpa_supplicant
ctrl_interface_group=0
update_config=1
```

2. Démarrer wpa_supplicant :

```
# wpa_supplicant -Dwext -i[interface] -cwpa_supplicant.conf
```

3. S'enregistrer auprès du AP avec `wpa_cli` et `wps_reg` :

```
# wpa_cli [interface]
> wps_reg [bssid] [wps_pin]
```

4. Une fois authentifié, sauvegarder la nouvelle configuration avec `save` :

```
> save
```

5. Lire le password dans le fichier `wpa_supplicant.conf` créé préalablement.

```
cat wpa_supplicant.conf
```

## FAQ

### L'output de wpa_reg me renvoie `Device or resource is busy`.

Il faut killer tout process qui pourrait vouloir utiliser les cartes réseaux. Un bon moyen pour lister les process susceptible de mobilisé la carte réseau est avec `airmon-ng check` ou `airmon-ng check kill` pour rapidement terminer ces process.

### wpa_reg ne réussie pas à se connecter

Si le router est loin, il se peut que wpa_reg prennne plusieurs minutes avant de s'associer et de se connecter correctement avec le pin wps. Il faut être patient !
