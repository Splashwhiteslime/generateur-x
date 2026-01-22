# timide.py

def get_defis(mode):
    """
    Retourne 20 défis pour le trait Timide.
    Focus : Briser la glace, sortir de sa zone de confort, rougissements et aveux.
    """
    
    defis = {
        "Mixte": [
            "PRÉSENTIEL : Regarde l'autre dans les yeux pendant 30 secondes sans parler et sans détourner le regard.",
            "WHATSAPP : Envoie un message avouant la chose la plus gênante qui t'excite chez l'autre.",
            "PRÉSENTIEL : Chuchote à l'oreille de l'autre un compliment osé que tu n'as jamais osé dire à voix haute.",
            "DISTANCE : Prends un selfie en train de rougir (ou en te cachant partiellement le visage) et envoie-le.",
            "PRÉSENTIEL : Laisse l'autre te tenir les mains et te raconter un souvenir érotique pendant que tu l'écoutes.",
            "WHATSAPP : Envoie un vocal de 10s où tu bégayes volontairement en disant ce que tu aimerais lui faire.",
            "PRÉSENTIEL : Autorise l'autre à soulever un seul vêtement de son choix pendant seulement 5 secondes.",
            "DISTANCE : Montre une petite partie de ta peau (épaule, cheville, hanche) à la caméra avec hésitation.",
            "PRÉSENTIEL : Demande à l'autre de fermer les yeux et donne-lui un baiser très rapide sur le coin des lèvres.",
            "WHATSAPP : Envoie la photo d'un objet qui te rappelle l'autre de façon sensuelle.",
            "PRÉSENTIEL : Cache tes yeux avec tes mains et laisse l'autre t'embrasser où il/elle veut.",
            "DISTANCE : Enlève un vêtement (comme une chaussette ou un accessoire) lentement devant la caméra.",
            "PRÉSENTIEL : Dis à voix haute trois parties du corps de l'autre qui te font perdre tes moyens.",
            "WHATSAPP : Envoie un message : 'J'ai très envie de toi, mais j'ai peur de te le montrer'.",
            "PRÉSENTIEL : Écris ton prénom avec ton doigt sur la peau nue de l'autre sans qu'il/elle ne regarde.",
            "DISTANCE : Montre ta lingerie à la caméra, mais juste un petit bout qui dépasse de ton vêtement.",
            "PRÉSENTIEL : Assieds-toi tout près de l'autre, épaule contre épaule, et reste ainsi sans bouger.",
            "WHATSAPP : Envoie une photo de tes pieds nus avec un message timide : 'Ils aimeraient te toucher'.",
            "PRÉSENTIEL : Laisse l'autre déboutonner un seul bouton de ton haut et reste ainsi pour le prochain tour.",
            "DISTANCE : Fais un bisou à l'écran de ton téléphone en fermant les yeux très fort."
        ],
        "F-F": [
            "PRÉSENTIEL : Effleure sa joue avec le dos de ta main et dis-lui qu'elle est magnifique.",
            "WHATSAPP : Envoie-lui : 'Tu m'intimides quand tu me regardes comme ça'.",
            "PRÉSENTIEL : Pose ta tête sur son épaule et ferme les yeux pendant qu'elle te caresse le bras.",
            "DISTANCE : Envoie une photo de toi en train de mordre ta lèvre par timidité.",
            "PRÉSENTIEL : Laisse-la te retirer tes chaussures et masser tes pieds en silence.",
            "WHATSAPP : Envoie un vocal où tu murmures son prénom très doucement.",
            "PRÉSENTIEL : Demande-lui si tu peux l'embrasser, et attends sa réponse avant de le faire.",
            "DISTANCE : Montre ton décolleté à la caméra pendant 2 secondes puis cache-le vite.",
            "PRÉSENTIEL : Reste blottie contre elle pendant une minute entière sans rien dire.",
            "WHATSAPP : Envoie une photo de ta main prête à attraper la sienne.",
            "PRÉSENTIEL : Laisse-la choisir une zone de ton corps (non intime) qu'elle peut embrasser.",
            "DISTANCE : Envoie un message décrivant ton premier sentiment quand tu l'as vue.",
            "PRÉSENTIEL : Donne-lui un baiser papillon (avec tes cils) sur la joue.",
            "WHATSAPP : Envoie : 'Je suis toute rouge à cause de tes défis'.",
            "PRÉSENTIEL : Propose-lui de te tenir la main pour le reste du jeu.",
            "DISTANCE : Fais un petit strip-tease, mais garde tes mains devant ta poitrine tout le long.",
            "PRÉSENTIEL : Laisse-la te murmurer quelque chose de coquin à l'oreille sans réagir.",
            "WHATSAPP : Envoie une photo de ton lit avec le message : 'Il y a de la place... si tu veux'.",
            "PRÉSENTIEL : Cache ton visage dans son cou et respire son parfum.",
            "DISTANCE : Montre tes jambes nues sous la table à la caméra avec un sourire gêné."
        ],
        "G-G": [
            "PRÉSENTIEL : Pose ta main sur son genou et laisse-la là pendant que vous parlez.",
            "DISTANCE : Envoie un message : 'Je ne sais pas trop comment te le dire, mais j'adore ton corps'.",
            "PRÉSENTIEL : Dis-lui quel trait de sa personnalité virile te rend nerveux.",
            "WHATSAPP : Envoie une photo de ton regard dans le miroir avec un air sérieux et timide.",
            "PRÉSENTIEL : Laisse-le te masser les épaules pour t'aider à te détendre.",
            "WHATSAPP : Envoie un vocal court : 'Tu me fais de l'effet'.",
            "PRÉSENTIEL : Demande-lui de te regarder fixement jusqu'à ce que tu baisses les yeux.",
            "DISTANCE : Montre tes bras nus à la caméra avec un petit mouvement de muscle hésitant.",
            "PRÉSENTIEL : Propose-lui un baiser sur le front ou la tempe.",
            "WHATSAPP : Envoie une photo de ton t-shirt préféré avec le message : 'Il sent mon parfum'.",
            "PRÉSENTIEL : Laisse-le choisir un vêtement que tu dois enlever.",
            "DISTANCE : Envoie un message décrivant ce que tu ressens quand il s'approche de toi.",
            "PRÉSENTIEL : Assieds-toi par terre aux pieds de son fauteuil/chaise.",
            "WHATSAPP : Envoie une photo de ton entrejambe (en pantalon) avec un emoji gêné.",
            "PRÉSENTIEL : Laisse-le te prendre dans ses bras pour un câlin de 20 secondes.",
            "DISTANCE : Montre ton torse nu, mais cache tes tétons avec tes bras croisés.",
            "PRÉSENTIEL : Dis-lui quelle partie de son visage tu préfères.",
            "WHATSAPP : Envoie : 'Je n'arrive pas à arrêter de penser à tes lèvres'.",
            "PRÉSENTIEL : Laisse-le te toucher la barbe ou les cheveux.",
            "DISTANCE : Envoie une vidéo de 5s où tu souris en regardant ailleurs."
        ]
    }
    
    return defis.get(mode, defis["Mixte"])