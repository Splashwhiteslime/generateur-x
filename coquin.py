# coquin.py

def get_defis(mode):
    """
    Retourne 20 défis pour le trait Coquin.
    Focus : Taquineries, jeux sensuels, contact ludique et esprit malicieux.
    """
    
    defis = {
        "Mixte": [
            "PRÉSENTIEL : Utilise le bout de ta langue pour tracer un chemin imaginaire sur son bras.",
            "WHATSAPP : Envoie un selfie en train de faire un clin d'œil avec une sucette ou une paille dans la bouche.",
            "PRÉSENTIEL : Glisse un glaçon ou un objet froid dans son dos et empêche-le/la de bouger pendant 10s.",
            "DISTANCE : Envoie un message : 'Devine la couleur de mes sous-vêtements. Si tu as juste, je t'envoie une photo'.",
            "PRÉSENTIEL : Mords-lui doucement l'épaule à travers son vêtement en faisant un petit bruit de prédateur.",
            "WHATSAPP : Envoie un vocal en chuchotant : 'Tu es un(e) très vilain(e) garçon/fille...'.",
            "PRÉSENTIEL : Chatouille l'autre dans une zone sensible jusqu'à ce qu'il/elle te supplie d'arrêter.",
            "DISTANCE : Fais un strip-tease de tes chaussettes de la façon la plus sexy possible face caméra.",
            "PRÉSENTIEL : Dessine un petit cœur avec tes lèvres sur une partie de son corps (hors visage).",
            "WHATSAPP : Envoie une photo de tes lèvres avec une trace de dent ou un peu de brillant.",
            "PRÉSENTIEL : Propose à l'autre de te donner une fessée de 'félicitations' pour ton audace.",
            "DISTANCE : Rapproche-toi de la caméra et fais semblant de lécher l'oreille de l'autre.",
            "PRÉSENTIEL : Souffle de l'air chaud dans son cou, puis juste après, de l'air froid.",
            "WHATSAPP : Envoie un message : 'Si on était seuls dans un ascenseur là, je te ferais...'.",
            "PRÉSENTIEL : Joue avec tes mains dans ses cheveux tout en lui racontant une bêtise sexy.",
            "DISTANCE : Montre un petit bout de ta peau que l'autre n'a pas encore vu ce soir.",
            "PRÉSENTIEL : Déboutonne le premier bouton de son haut et souffle sur sa peau.",
            "WHATSAPP : Envoie une photo de ta main prête à faire une bêtise.",
            "PRÉSENTIEL : Échange un vêtement léger (bijou, montre, accessoire) avec l'autre pour le reste du jeu.",
            "DISTANCE : Envoie une vidéo de 5s où tu mords ta lèvre avec un regard malicieux."
        ],
        "F-F": [
            "PRÉSENTIEL : Fais-lui un bisou sur le nez, puis un bisou mordu sur le cou.",
            "WHATSAPP : Envoie-lui : 'J'ai envie de te taquiner jusqu'à ce que tu craques'.",
            "PRÉSENTIEL : Utilise tes cheveux pour lui caresser le visage et le décolleté.",
            "DISTANCE : Montre ta culotte qui dépasse de ton jean/jupe à la caméra.",
            "PRÉSENTIEL : Assieds-toi sur ses genoux et rebondis légèrement en riant.",
            "WHATSAPP : Envoie un selfie avec une trace de rouge à lèvres sur ta propre épaule.",
            "PRÉSENTIEL : Lèche une goutte d'eau sur ton doigt avant de le poser sur ses lèvres.",
            "DISTANCE : Fais une moue boudeuse et sexy devant l'écran.",
            "PRÉSENTIEL : Tire doucement sur les bretelles de son haut/soutien-gorge et lâche-les.",
            "WHATSAPP : Envoie une photo de tes jambes nues entrelacées avec un coussin.",
            "PRÉSENTIEL : Murmure-lui une blague cochonne à l'oreille.",
            "DISTANCE : Montre ton dos nu et fais un clin d'œil par-dessus ton épaule.",
            "PRÉSENTIEL : Fais-lui un massage des mains en insistant sur les zones charnues.",
            "WHATSAPP : Envoie : 'Tu es mon jouet préféré ce soir'.",
            "PRÉSENTIEL : Mime un baiser passionné dans le vide en la regardant.",
            "DISTANCE : Lèche un glaçon de façon très suggestive face caméra.",
            "PRÉSENTIEL : Laisse-la te donner une petite tape sur les fesses.",
            "WHATSAPP : Envoie une photo de ton décolleté avec un emoji 'secret'.",
            "PRÉSENTIEL : Propose-lui de te mettre du parfum dans le cou.",
            "DISTANCE : Envoie un baiser soufflé très bruyant vers l'objectif."
        ],
        "G-G": [
            "PRÉSENTIEL : Donne-lui un coup d'épaule amical puis plaque-le contre toi pour un câlin rapide.",
            "DISTANCE : Envoie un message : 'T'as de la chance que je sois loin, sinon...'.",
            "PRÉSENTIEL : Mords ton t-shirt et tire dessus en le regardant de haut en bas.",
            "WHATSAPP : Envoie une photo de ton bras avec tes veines apparentes et un message taquin.",
            "PRÉSENTIEL : Propose un duel de chatouilles : le perdant finit torse nu.",
            "DISTANCE : Montre l'élastique de ton caleçon à la caméra en tirant dessus.",
            "PRÉSENTIEL : Pose ton pied entre ses jambes (si vous êtes assis) et bouge-le un peu.",
            "WHATSAPP : Envoie un vocal avec ton rire le plus charmeur.",
            "PRÉSENTIEL : Saisis sa ceinture et tire-le vers toi avec un sourire provocateur.",
            "DISTANCE : Envoie une photo de toi en train de boire à la bouteille de façon virile.",
            "PRÉSENTIEL : Mords-lui l'avant-bras doucement.",
            "WHATSAPP : Envoie : 'Je parie que tu ne tiens pas 1 min sans me regarder'.",
            "PRÉSENTIEL : Ébouriffe ses cheveux puis recoiffe-le avec tes doigts.",
            "DISTANCE : Montre ton torse nu sous un angle original (en contre-plongée).",
            "PRÉSENTIEL : Donne-lui une fessée 'de pote' mais qui dure un peu trop longtemps.",
            "WHATSAPP : Envoie une photo de tes mains avec le message 'Elles sont très joueuses'.",
            "PRÉSENTIEL : Lèche le bord de ton verre en le fixant.",
            "DISTANCE : Fais une pose de super-héros mais uniquement en caleçon.",
            "PRÉSENTIEL : Propose de lui faire un tatouage temporaire au stylo sur la peau.",
            "WHATSAPP : Envoie : 'T'es mignon quand tu réfléchis à ton défi'."
        ]
    }
    
    return defis.get(mode, defis["Mixte"])