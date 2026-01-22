# souple.py

def get_defis(mode):
    """
    Retourne 20 défis pour le trait Souple.
    Focus : Agilité, flexibilité, positions acrobatiques et étirements suggestifs.
    """
    
    defis = {
        "Mixte": [
            "PRÉSENTIEL : Mets-toi debout et touche tes orteils sans plier les genoux pendant que l'autre regarde ton dos.",
            "WHATSAPP : Envoie une photo de toi en faisant un grand écart (ou le maximum possible) en sous-vêtements.",
            "PRÉSENTIEL : Place une jambe sur l'épaule de l'autre et reste ainsi pendant que vous discutez.",
            "DISTANCE : Mets-toi à quatre pattes face caméra, cambre ton dos au maximum et lève une jambe en l'air.",
            "PRÉSENTIEL : Allonge-toi sur le dos et ramène tes genoux derrière tes oreilles en fixant l'autre.",
            "WHATSAPP : Envoie une photo de toi dans une position de 'pont' (arqué sur les mains et les pieds).",
            "PRÉSENTIEL : Assieds-toi au sol, écarte les jambes au maximum et laisse l'autre s'appuyer sur ton dos pour t'aider à descendre.",
            "DISTANCE : Fais une vidéo de 10s en faisant une rotation lente du bassin très cambrée.",
            "PRÉSENTIEL : Enlace l'autre avec tes jambes alors qu'il/elle est debout, sans toucher le sol.",
            "WHATSAPP : Envoie une photo de toi en train d'étirer tes bras derrière ton dos, mettant ta poitrine en valeur.",
            "PRÉSENTIEL : Fais une roue ou une figure d'agilité simple en sous-vêtements devant l'autre.",
            "DISTANCE : Montre à la caméra que tu peux toucher ton pied avec ta tête (ou presque).",
            "PRÉSENTIEL : Mets-toi en position de fente très basse et laisse l'autre caresser tes cuisses tendues.",
            "WHATSAPP : Envoie une photo de toi cambré(e) contre un mur, vue de profil.",
            "PRÉSENTIEL : Allonge-toi et lève les jambes à la verticale, puis écarte-les lentement devant l'autre.",
            "DISTANCE : Pose ton téléphone au sol et accroupis-toi au-dessus de l'objectif très bas.",
            "PRÉSENTIEL : Essaye de faire le grand écart facial et demande à l'autre de s'asseoir face à toi.",
            "WHATSAPP : Envoie une photo de ta jambe levée très haut (contre un encadrement de porte par exemple).",
            "PRÉSENTIEL : Laisse l'autre manipuler tes membres pour te mettre dans la position la plus tordue possible.",
            "DISTANCE : Fais une séance d'étirements de 30s en direct en gémissant doucement à cause de l'effort."
        ],
        "F-F": [
            "PRÉSENTIEL : Allonge-toi sur elle et plie tes jambes pour que tes pieds touchent ta tête.",
            "WHATSAPP : Envoie-lui une photo de toi dans une position de yoga 'Chien tête en bas' en culotte.",
            "PRÉSENTIEL : Fais un grand écart et laisse-la s'installer entre tes jambes pour te masser.",
            "DISTANCE : Envoie une vidéo où tu montres ta souplesse de dos en te cambrant face au miroir.",
            "PRÉSENTIEL : Enlace sa taille avec tes deux jambes et bascule ton corps vers l'arrière.",
            "WHATSAPP : Envoie une photo de ta jambe levée derrière ta tête (Vue Unique).",
            "PRÉSENTIEL : Mets-toi en pont au-dessus d'elle et embrasse-la dans cette position renversée.",
            "DISTANCE : Montre comment tu peux attraper tes mains derrière ton dos en passant par-dessus tes épaules.",
            "PRÉSENTIEL : Pose tes pieds sur ses épaules et laisse-la embrasser tes chevilles et tes mollets.",
            "WHATSAPP : Envoie une photo de toi accroupie, les genoux très écartés, avec un regard provocateur.",
            "PRÉSENTIEL : Fais une chandelle et écarte les jambes au maximum au-dessus de son visage.",
            "DISTANCE : Vidéo de toi en train de passer ta jambe par-dessus ton épaule.",
            "PRÉSENTIEL : Laisse-la tester ta souplesse en poussant doucement tes jambes vers ton torse.",
            "WHATSAPP : Envoie une photo de ton dos cambré à l'extrême vue de derrière.",
            "PRÉSENTIEL : Accroupis-toi sur elle sans poser ton poids et bouge tes hanches avec souplesse.",
            "DISTANCE : Fais un étirement des fessiers très suggestif face à la caméra.",
            "PRÉSENTIEL : Essaye d'attraper tes chevilles avec tes mains en passant entre tes jambes.",
            "WHATSAPP : Envoie une photo de toi en 'position du lotus' mais totalement nue.",
            "PRÉSENTIEL : Utilise ta souplesse pour l'embrasser sans utiliser tes mains pour te tenir.",
            "DISTANCE : Montre-lui une pose de gymnaste érotique que tu as apprise."
        ],
        "G-G": [
            "PRÉSENTIEL : Fais une pompe en levant une jambe très haut en arrière pendant qu'il regarde.",
            "DISTANCE : Envoie une photo de toi en train de faire un pont, mettant en avant ton entrejambe.",
            "PRÉSENTIEL : Pose ton pied sur son torse et étire ta jambe au maximum.",
            "WHATSAPP : Envoie une photo de tes jambes nues très écartées avec un message sur ton agilité.",
            "PRÉSENTIEL : Plie-toi en deux pour toucher le sol et laisse-le te donner une fessée dans cette pose.",
            "DISTANCE : Montre à la caméra que tu peux faire le grand écart (ou essayer sérieusement).",
            "PRÉSENTIEL : Porte-le et accroupis-toi (squat profond) en gardant le dos bien droit.",
            "WHATSAPP : Envoie une vidéo de toi en train de faire des rotations de hanches très fluides.",
            "PRÉSENTIEL : Allonge-toi et lève tes jambes pour qu'il puisse voir ta souplesse de bassin.",
            "DISTANCE : Prends une photo de toi en train d'étirer tes pectoraux contre un mur.",
            "PRÉSENTIEL : Mets-toi en équilibre sur les mains (ou contre un mur) et reste 10 secondes.",
            "WHATSAPP : Envoie une photo de toi cambré, mettant en valeur la cambrure de tes reins.",
            "PRÉSENTIEL : Laisse-le s'asseoir sur ton dos pendant que tu es en position d'étirement au sol.",
            "DISTANCE : Fais une démonstration de ta souplesse de bras et d'épaules.",
            "PRÉSENTIEL : Accroupis-toi face à lui et écarte les genoux au maximum.",
            "WHATSAPP : Envoie une photo de toi en train de faire un exercice de souplesse nu.",
            "PRÉSENTIEL : Fais une fente avant et laisse-le appuyer sur tes hanches pour descendre plus bas.",
            "DISTANCE : Montre comment tu peux plier ton corps de façon impressionnante face caméra.",
            "PRÉSENTIEL : Attrape ses mains et penche-toi en arrière au maximum en comptant sur lui.",
            "WHATSAPP : Envoie un message : 'Imagine ce que ma souplesse permet de faire au lit'."
        ]
    }
    
    return defis.get(mode, defis["Mixte"])