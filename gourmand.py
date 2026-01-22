# gourmand.py

def get_defis(mode):
    """
    Retourne 20 défis pour le trait Gourmand.
    Focus : Nourriture, sensations gustatives, chaud/froid et contact oral.
    """
    
    defis = {
        "Mixte": [
            "PRÉSENTIEL : Verse une goutte de ta boisson dans son cou et récupère-la avec ta langue.",
            "WHATSAPP : Envoie une photo de toi en train de manger un fruit (fraise, banane) de façon très suggestive.",
            "PRÉSENTIEL : Trempe ton doigt dans quelque chose de sucré et laisse l'autre le sucer longuement.",
            "DISTANCE : Prends un glaçon en bouche face caméra et laisse-le fondre en regardant l'autre fixement.",
            "PRÉSENTIEL : Place un aliment (bonbon, fruit) entre tes lèvres et donne-le à l'autre sans utiliser les mains.",
            "WHATSAPP : Envoie un vocal : décrit le goût que tu penses que sa peau a en ce moment.",
            "PRÉSENTIEL : Utilise de la chantilly ou du chocolat pour dessiner un petit motif sur sa poitrine, puis lèche-le.",
            "DISTANCE : Verse un peu de liquide sur ton propre décolleté/torse face caméra et lèche ce que tu peux atteindre.",
            "PRÉSENTIEL : Mange un carré de chocolat et embrasse l'autre langoureusement pour lui faire goûter.",
            "WHATSAPP : Envoie une photo 'Vue Unique' de tes lèvres brillantes après avoir bu ou mangé quelque chose de gras.",
            "PRÉSENTIEL : Laisse l'autre verser un filet de boisson sur ton ventre et le boire directement sur ta peau.",
            "DISTANCE : Montre à la caméra comment tu mangerais l'autre si il/elle était un dessert.",
            "PRÉSENTIEL : Ferme les yeux. L'autre doit placer un aliment sur une partie de ton corps et tu dois deviner quoi et où.",
            "WHATSAPP : Envoie le nom de l'aliment que tu aimerais étaler sur le corps de l'autre maintenant.",
            "PRÉSENTIEL : Lèche le bord d'un verre, puis passe ta langue sur le lobe d'oreille de l'autre.",
            "DISTANCE : Fais une vidéo de 5s où tu croques dans un aliment en fermant les yeux de plaisir.",
            "PRÉSENTIEL : Tartine tes lèvres d'un produit collant (miel, sirop) et embrasse l'autre partout sauf sur la bouche.",
            "WHATSAPP : Envoie une photo de ton frigo avec le message 'Choisis mon prochain accessoire de plaisir'.",
            "PRÉSENTIEL : Fais couler de l'eau tiède sur les mains de l'autre tout en le/la fixant avec envie.",
            "DISTANCE : Suce ton propre doigt face caméra en imaginant que c'est une partie du corps de l'autre."
        ],
        "F-F": [
            "PRÉSENTIEL : Verse un peu de champagne ou de vin dans son décolleté et lèche chaque goutte.",
            "WHATSAPP : Envoie-lui une photo de ta bouche avec une cerise ou un fruit rouge.",
            "PRÉSENTIEL : Utilise du miel pour lui 'coller' un baiser sur le cou.",
            "DISTANCE : Envoie un vocal en décrivant le goût de son intimité tel que tu l'imagines.",
            "PRÉSENTIEL : Mangez un fruit ensemble, chacun mordant d'un côté en même temps.",
            "WHATSAPP : Envoie une photo de tes seins avec une goutte de boisson qui perle.",
            "PRÉSENTIEL : Lèche une trace de sucre sur son épaule ou sa clavicule.",
            "DISTANCE : Montre à la caméra comment tu lèches une cuillère de façon érotique.",
            "PRÉSENTIEL : Propose-lui de te nourrir à la main alors que tu es à genoux.",
            "WHATSAPP : Envoie : 'Tu es mon fruit défendu', suivi d'une photo de tes lèvres.",
            "PRÉSENTIEL : Laisse-la étaler un peu de baume à lèvres sur tes seins avec sa bouche.",
            "DISTANCE : Verse du lait ou du jus sur tes mains et frotte-les face caméra.",
            "PRÉSENTIEL : Fais-lui un massage avec une huile parfumée comestible.",
            "WHATSAPP : Envoie une photo de ta langue bien rose avec un message coquin.",
            "PRÉSENTIEL : Mords doucement un fruit et laisse le jus couler sur son bras avant de le lécher.",
            "DISTANCE : Simule une dégustation très sensuelle d'un yaourt ou d'une crème face caméra.",
            "PRÉSENTIEL : Laisse-la choisir un aliment dans la cuisine et l'utiliser sur toi comme elle veut.",
            "WHATSAPP : Envoie une photo de toi avec de la chantilly sur un doigt.",
            "PRÉSENTIEL : Donne-lui un baiser qui a le goût de ton dernier verre.",
            "DISTANCE : Montre ton entrejambe et dis-lui quel dessert tu aimerais manger là-dessus."
        ],
        "G-G": [
            "PRÉSENTIEL : Verse un shot d'alcool sur ses abdos et bois-le directement.",
            "DISTANCE : Envoie une photo de toi en train de mordre dans un morceau de viande ou un fruit avec force.",
            "PRÉSENTIEL : Lèche le sel ou le sucre sur son cou après avoir bu un verre.",
            "WHATSAPP : Envoie un message : 'J'ai faim de toi, et je ne parle pas de nourriture'.",
            "PRÉSENTIEL : Mords-lui la lèvre après avoir mangé quelque chose de pimenté ou de fort.",
            "DISTANCE : Envoie une vidéo où tu bois une canette de façon très virile et mouillée.",
            "PRÉSENTIEL : Propose-lui de lécher de la nourriture sur tes muscles contractés.",
            "WHATSAPP : Envoie une photo de tes dents avec le message 'Prêt à te dévorer'.",
            "PRÉSENTIEL : Utilise un glaçon pour masser son entrejambe par-dessus le pantalon.",
            "DISTANCE : Montre ton torse nu et verse un peu d'eau dessus face caméra.",
            "PRÉSENTIEL : Partagez un chewing-gum ou un bonbon lors d'un baiser très court.",
            "WHATSAPP : Envoie une photo de ta main tenant un verre avec un message sur la soirée.",
            "PRÉSENTIEL : Lèche ton pouce et passe-le sur ses lèvres pour les humidifier.",
            "DISTANCE : Montre tes bras et dis-lui quel goût ta sueur doit avoir après le sport.",
            "PRÉSENTIEL : Laisse-le te nourrir avec l'aliment de son choix.",
            "WHATSAPP : Envoie un selfie avec une bouteille au goulot et un regard provocateur.",
            "PRÉSENTIEL : Écrase un fruit mou (comme une baie) sur son torse et lèche-le.",
            "DISTANCE : Fais une démonstration de force en ouvrant quelque chose avec tes dents.",
            "PRÉSENTIEL : Demande-lui quel est son goût préféré et essaye de le trouver sur sa peau.",
            "WHATSAPP : Envoie : 'Ce soir, le menu c'est toi'."
        ]
    }
    
    return defis.get(mode, defis["Mixte"])