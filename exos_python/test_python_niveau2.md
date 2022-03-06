## Test python : mise en forme d'un fichier json. ##

### Objectif :###   

*** Nous voulons mettre en forme un json d'un format vers un autre. ***


Nous recevons des fichiers contenant des commandes (orders); ces commandes contiennent des informations,
2 catégories d'information nous intéressent particulièrement :
- les tickets

- les productItemAttributeOptions


Le but est de générer un nouveau json ou l'on aura un tableau de tickets avec les informations de l'order auquel il est associé.

Format d'entrée simplifié :
```
   ordersWithDetails{
     items:[
          {
            ...  
          },
          {
          infos
          user:{}
          salesChannel:{}
          orderItems: [
                      {
                      infos_order
                      product:{
                              infos_products
                              productItemAttributeOptions: []
                              }
                      tickets:[
                              {
                              infos_tickets  
                              },
                              {
                              ...  
                              }
                              ]
                      },
                      {
                      ...  
                      }
                      ]
            },
            {
            ...  
            }
          ]
```

Format de sortie simplifié désiré:   
```
[
{
...  
},
{
infos
user:{}
salesChannel:{}
infos_order
infos_products
infos_tickets
productItemAttributeOptions:{}
},
{
...
}
]
```

#### Attention ! ####
- on dupliquera toutes les infos de la commande sur chaque ticket
- pour les informations de productItemAttributeOptions on transformera le tableau en liste (voir exemple ci-dessous).   
pour les items de la liste on prendra le ProductAttribute -> code auquel au aura associé un nombre selon le nombre de récurrence.


### Exemple  productItemAttributeOptions ###   
Avant :
```
  "productItemAttributeOptions": [
    {
      "__typename": "ProductItemAttributeOption",
      "productAttribute": {
        "__typename": "ProductAttribute",
        "code": "Category",
        "label": "Catégorie"
      },
      "productAttributeOption": {
        "__typename": "ProductAttributeOption",
        "code": "c45ecc7d",
        "label": "VIP"
      }
    },
    {
      "__typename": "ProductItemAttributeOption",
      "productAttribute": {
        "__typename": "ProductAttribute",
        "code": "SalesChannel",
        "label": "Canal de vente"
      },
      "productAttributeOption": {
        "__typename": "ProductAttributeOption",
        "code": "8bc5a233917",
        "label": "Guichet"
      }
    },
    {
      "__typename": "ProductItemAttributeOption",
      "productAttribute": {
        "__typename": "ProductAttribute",
        "code": "SalesChannel",
        "label": "Canal de vente"
      },
      "productAttributeOption": {
        "__typename": "ProductAttributeOption",
        "code": "83748f947c9",
        "label": "Web"
      }
    }
  ]
```    

Aprés transformation [] vers {}
```
"productItemAttributeOptions": {
    "productAttribute_Category_1": {
      "__typename": "ProductItemAttributeOption",
      "productAttribute": {
        "__typename": "ProductAttribute",
        "code": "Category",
        "label": "Catégorie"
      },
      "productAttributeOption": {
        "__typename": "ProductAttributeOption",
        "code": "c45ecc7d",
        "label": "VIP"
      }
    },
    "productAttribute_SalesChannel_1": {
      "__typename": "ProductItemAttributeOption",
      "productAttribute": {
        "__typename": "ProductAttribute",
        "code": "SalesChannel",
        "label": "Canal de vente"
      },
      "productAttributeOption": {
        "__typename": "ProductAttributeOption",
        "code": "8bc5a233917",
        "label": "Guichet"
      }
    },
    "productAttribute_SalesChannel_2": {
      "__typename": "ProductItemAttributeOption",
      "productAttribute": {
        "__typename": "ProductAttribute",
        "code": "SalesChannel",
        "label": "Canal de vente"
      },
      "productAttributeOption": {
        "__typename": "ProductAttributeOption",
        "code": "83748f947c9",
        "label": "Web"
      }
    }
  }

```
### Todo ###
- Lire les fichiers contenu dans le répertoire ci-joint.
- Faire les traitements voulus en python.
- Générer un fichier json de sortie.
- Faire une petite doc explicative.
