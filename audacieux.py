# tendance_lesbienne.py

def get_defis(mode):
    """
    Retourne 20 défis pour le trait Tendance Lesbienne.
    Focus : Sensualité féminine, contact peau à peau, exploration et douceur érotique.
    """
    
    defis = {
        "F-F": [
            "PRÉSENTIEL : Caresse ses cheveux en lui murmurant à l'oreille ce que tu trouves de plus sexy chez une femme.",
            "WHATSAPP : Envoie-lui un message vocal en décrivant la sensation de ses mains sur ta peau.",
            "PRÉSENTIEL : Trace le contour de ses lèvres avec ta langue, très lentement, sans l'embrasser vraiment.",
            "DISTANCE : Envoie une photo de ton décolleté avec le message : 'Imagine ma tête ici'.",
            "PRÉSENTIEL : Masse-lui les mains avec de la crème en entrelaçant tes doigts aux siens longuement.",
            "WHATSAPP : Envoie une photo de tes lèvres entrouvertes et humides (Vue Unique).",
            "PRÉSENTIEL : Allonge-toi la tête sur ses genoux et laisse-la caresser ton visage pendant 2 minutes.",
            "DISTANCE : Décris par message détaillé ta première attirance pour une femme.",
            "PRÉSENTIEL : Embrasse chaque doigt de sa main l'un après l'autre en la fixant dans les yeux.",
            "WHATSAPP : Envoie un selfie de toi portant l'un de ses vêtements (si possible) ou quelque chose qui lui appartient.",
            "PRÉSENTIEL : Effleure sa poitrine avec le bout de tes ongles, très légèrement, jusqu'à ce qu'elle frissonne.",
            "DISTANCE : Fais une vidéo de 10s où tu caresses ton propre cou et tes clavicules de façon sensuelle.",
            "PRÉSENTIEL : Enlève ton haut et demande-lui de masser ton dos nu avec ses lèvres.",
            "WHATSAPP : Envoie : 'Je rêve de sentir ton parfum sur mon oreiller', suivi d'une photo de ton lit.",
            "PRÉSENTIEL : Assieds-toi face à elle, colle tes genoux aux siens et ne romps pas le contact visuel pendant 1 min.",
            "DISTANCE : Montre à la caméra comment tu embrasserais ton propre bras si c'était le sien.",
            "PRÉSENTIEL : Glisse tes mains sous sa taille et rapproche-la de toi pour un baiser de 20 secondes.",
            "WHATSAPP : Envoie une photo 'Vue Unique' de tes jambes nues entrelacées (ou imagine-les).",
            "PRÉSENTIEL : Lèche-lui le lobe de l'oreille et murmure-lui un secret inavouable.",
            "DISTANCE : Simule un moment de tendresse érotique avec un coussin devant la caméra."
        ],
        "Mixte": [
            "PRÉSENTIEL : Explique à l'autre ce qui t'attire chez le même sexe avec des détails physiques.",
            "WHATSAPP : Envoie une photo d'une célébrité féminine qui te fait craquer sexuellement.",
            "PRÉSENTIEL : Fais un compliment très poussé sur la douceur de la peau de l'autre.",
            "DISTANCE : Envoie un vocal décrivant une expérience ou un fantasme saphique que tu as eu.",
            "PRÉSENTIEL : Caresse le dos de l'autre en faisant des cercles de plus en plus bas.",
            "WHATSAPP : Envoie une photo de tes lèvres avec le message : 'Elles sont très impatientes'.",
            "PRÉSENTIEL : Embrasse l'autre dans le cou, juste sous l'oreille, pendant 10 secondes.",
            "DISTANCE : Montre ton profil face caméra en mettant en avant tes courbes féminines.",
            "PRÉSENTIEL : Propose à l'autre de te brosser les cheveux ou de te masser la nuque.",
            "WHATSAPP : Envoie un message décrivant la texture de la lingerie que tu préfères toucher.",
            "PRÉSENTIEL : Laisse l'autre toucher tes hanches pendant que tu danses doucement.",
            "DISTANCE : Prends une photo de ta main posée sur ta poitrine et envoie-la.",
            "PRÉSENTIEL : Mords doucement ton propre doigt en regardant l'autre avec envie.",
            "WHATSAPP : Envoie une photo de ton cou nu avec le message : 'Libre pour tes lèvres'.",
            "PRÉSENTIEL : Rapproche-toi et respire l'odeur de l'autre en fermant les yeux.",
            "DISTANCE : Fais un clin d'œil et envoie un baiser soufflé à la caméra.",
            "PRÉSENTIEL : Effleure l'intérieur de son bras avec tes lèvres.",
            "WHATSAPP : Envoie un message : 'J'aime quand tu me regardes comme ça'.",
            "PRÉSENTIEL : Tiens la main de l'autre et caresse sa paume avec ton pouce.",
            "DISTANCE : Envoie une photo de tes pieds nus avec un message taquin."
        ],
        "G-G": [
            "PRÉSENTIEL : Dis un compliment sur la beauté des mains ou du visage de l'autre (côté doux).",
            "DISTANCE : Envoie un message décrivant ce que tu trouves de plus 'esthétique' chez un homme.",
            "PRÉSENTIEL : Pose ta tête sur son épaule pendant tout le prochain tour.",
            "WHATSAPP : Envoie une chanson sensuelle que tu aimerais écouter avec lui.",
            "PRÉSENTIEL : Caresse-lui le bras avec le bout des doigts pour lui donner des frissons.",
            "DISTANCE : Prends une photo de ton regard dans le miroir et envoie-la.",
            "PRÉSENTIEL : Propose un massage du visage ou des tempes très lent.",
            "WHATSAPP : Envoie un message : 'Ta présence m'apaise et m'excite à la fois'.",
            "PRÉSENTIEL : Reste très proche de lui, épaule contre épaule, sans rien dire pendant 1 min.",
            "DISTANCE : Envoie une photo de tes mains avec un message sur leur douceur.",
            "PRÉSENTIEL : Murmure un compliment sincère et profond à son oreille.",
            "WHATSAPP : Envoie une photo de toi dans une tenue confortable et relax.",
            "PRÉSENTIEL : Touche ses cheveux et dis-lui s'ils sont doux.",
            "DISTANCE : Envoie un vocal où tu racontes un souvenir agréable avec lui.",
            "PRÉSENTIEL : Propose de lui tenir la main pendant que vous discutez.",
            "WHATSAPP : Envoie un emoji qui représente ton humeur actuelle par rapport à lui.",
            "PRÉSENTIEL : Regarde-le dans les yeux et souris-lui sincèrement sans raison.",
            "DISTANCE : Envoie une photo d'un détail de ta peau (tatouage, grain de beauté).",
            "PRÉSENTIEL : Fais-lui un câlin long et silencieux (30 secondes).",
            "WHATSAPP : Envoie un message : 'J'aime bien ce petit jeu entre nous'."
        ]
    }
    
    return defis.get(mode, defis["F-F"])