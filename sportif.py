# sportif.py

def get_defis(mode):
    """
    Retourne 20 défis pour le trait Sportif.
    Focus : Endurance, cardio, transpiration sexy et démonstration de force.
    """
    
    defis = {
        "Mixte": [
            "PRÉSENTIEL : Fais 15 pompes au-dessus de l'autre, en descendant le plus près possible de son visage à chaque fois.",
            "WHATSAPP : Envoie une photo de ton corps après avoir fait 20 jumpings jacks, pour montrer ta peau un peu brillante.",
            "PRÉSENTIEL : Fais la planche (gainage) pendant 1 minute pendant que l'autre s'assoit ou pose ses mains sur ton dos.",
            "DISTANCE : Fais une série de 20 squats face caméra en portant un vêtement très serré.",
            "PRÉSENTIEL : Porte l'autre dans tes bras (style mariés) et fais le tour de la pièce sans t'arrêter.",
            "WHATSAPP : Envoie un message vocal où on entend ton souffle court après un effort intense de 30 secondes.",
            "PRÉSENTIEL : Fais 20 fentes sautées en restant en sous-vêtements devant l'autre.",
            "DISTANCE : Montre tes muscles (bras ou jambes) à la caméra et contracte-les au maximum pendant 10s.",
            "PRÉSENTIEL : Mets-toi en position de chaise contre le mur et laisse l'autre s'asseoir sur tes genoux le plus longtemps possible.",
            "WHATSAPP : Envoie une photo de ta bouteille d'eau que tu verses sur ton cou pour te rafraîchir.",
            "PRÉSENTIEL : Allonge-toi et lève l'autre avec tes jambes (la presse humaine) 5 fois de suite.",
            "DISTANCE : Fais une démonstration de ton exercice de sport préféré en version 'très suggestive'.",
            "PRÉSENTIEL : Fais du saut à la corde imaginaire pendant 1 min en étant torse nu ou en brassière.",
            "WHATSAPP : Envoie une photo de tes abdos contractés après une série de crunchs.",
            "PRÉSENTIEL : Défie l'autre : le premier qui touche ses pieds 30 fois gagne le droit de déshabiller l'autre.",
            "DISTANCE : Fais du vélo imaginaire sur le dos face caméra pendant 45 secondes en gémissant de fatigue.",
            "PRÉSENTIEL : Porte l'autre sur ton dos et fais 10 pompes ou 10 squats (selon ta force).",
            "WHATSAPP : Envoie un selfie 'post-effort' avec les cheveux décoiffés et le regard fatigué.",
            "PRÉSENTIEL : Laisse l'autre essuyer la sueur sur ton front ou ton cou avec sa langue ou ses doigts.",
            "DISTANCE : Enlève ton haut de sport (ou t-shirt) face caméra en montrant tes muscles congestionnés."
        ],
        "F-F": [
            "PRÉSENTIEL : Fais 20 squats et à chaque remontée, donne-lui un petit baiser rapide.",
            "WHATSAPP : Envoie-lui une photo de ton legging de sport de dos, bien moulant.",
            "PRÉSENTIEL : Allonge-toi au sol, elle se met en gainage au-dessus de toi et vous devez tenir 30s.",
            "DISTANCE : Envoie une vidéo de toi en train de faire des étirements après le sport en tenue légère.",
            "PRÉSENTIEL : Porte-la sur tes hanches et essaye de marcher le plus longtemps possible.",
            "WHATSAPP : Envoie un vocal où tu décris à quel point l'effort physique te donne envie d'elle.",
            "PRÉSENTIEL : Fais une série de fessiers (levés de bassin) pendant qu'elle pose sa main sur ton ventre.",
            "DISTANCE : Montre ton ventre plat ou tes courbes à la caméra après une séance d'abdos.",
            "PRÉSENTIEL : Fais la roue ou une figure acrobatique et demande-lui de noter ta performance.",
            "WHATSAPP : Envoie une photo de ton décolleté de sport avec quelques gouttes de sueur.",
            "PRÉSENTIEL : Masse ses muscles après qu'elle ait fait 10 pompes pour l'aider à récupérer.",
            "DISTANCE : Fais une danse cardio très rythmée et sexy devant l'écran.",
            "PRÉSENTIEL : Essayez de faire des pompes synchronisées face à face.",
            "WHATSAPP : Envoie une photo de tes baskets et de tes jambes nues avec le message 'Prête à courir vers toi'.",
            "PRÉSENTIEL : Fais 30 secondes de 'mountain climbers' en la fixant intensément.",
            "DISTANCE : Montre comment tu es souple après t'être échauffée face caméra.",
            "PRÉSENTIEL : Laisse-la s'asseoir sur tes hanches pendant que tu fais des relevés de buste.",
            "WHATSAPP : Envoie une photo de toi en brassière de sport avec un regard de défi.",
            "PRÉSENTIEL : Course de vitesse dans la maison : la dernière arrivée enlève sa culotte.",
            "DISTANCE : Fais des fentes latérales en montrant bien le travail de tes jambes à l'écran."
        ],
        "G-G": [
            "PRÉSENTIEL : Fais 20 pompes claquées devant lui pour montrer ta puissance.",
            "DISTANCE : Envoie une photo de tes bras (biceps) contractés au maximum avec tes veines saillantes.",
            "PRÉSENTIEL : Soulève-le du sol et tiens-le en l'air pendant au moins 15 secondes.",
            "WHATSAPP : Envoie un message : 'Imagine ma force entre tes jambes ce soir'.",
            "PRÉSENTIEL : Faites une séance de gainage face à face, le premier qui tombe enlève son caleçon.",
            "DISTANCE : Enlève ton t-shirt de sport mouillé face caméra et jette-le vers l'objectif.",
            "PRÉSENTIEL : Fais des tractions (si possible) ou des squats avec lui sur ton dos.",
            "WHATSAPP : Envoie une photo de tes cuisses contractées après une série de jambes.",
            "PRÉSENTIEL : Propose un bras de fer : le gagnant donne un ordre sportif et sexy au perdant.",
            "DISTANCE : Montre ton dos nu et contracte tes dorsaux devant la caméra.",
            "PRÉSENTIEL : Fais 10 burpees le plus vite possible, puis laisse-le écouter ton cœur battre.",
            "WHATSAPP : Envoie un selfie de toi torse nu avec le message 'Coup de chaud, j'ai besoin de toi'.",
            "PRÉSENTIEL : Lutte amicale au sol : celui qui immobilise l'autre gagne un baiser forcé.",
            "DISTANCE : Fais une série de dips sur une chaise en montrant tes triceps à l'écran.",
            "PRÉSENTIEL : Sers-lui de poids : il doit essayer de te soulever 5 fois.",
            "WHATSAPP : Envoie une vidéo de toi en train de boxer dans le vide, très énergique.",
            "PRÉSENTIEL : Reste torse nu et fais des mouvements de musculation lents pour qu'il voie tes muscles bouger.",
            "DISTANCE : Montre ton entrejambe dans ton short de sport serré et demande-lui s'il voit l'effort.",
            "PRÉSENTIEL : Fais 50 abdos pendant qu'il te tient les chevilles.",
            "WHATSAPP : Envoie une photo de ton corps brillant sous la lumière avec un message viril."
        ]
    }
    
    return defis.get(mode, defis["Mixte"])