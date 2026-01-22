# menteur.py

def get_defis(mode):
    """
    Retourne 20 défis pour le trait Menteur.
    Focus : Bluff, secrets, vérité ou mensonge et manipulation psychologique.
    """
    
    defis = {
        "Mixte": [
            "PRÉSENTIEL : Raconte deux fantasmes à l'autre : un vrai et un faux. S'il/elle se trompe, il/elle enlève un vêtement.",
            "WHATSAPP : Envoie un message : 'Je ne porte pas de sous-vêtements'. L'autre doit deviner si tu mens. Si il/elle perd, il/elle doit t'envoyer une photo osée.",
            "PRÉSENTIEL : Regarde l'autre dans les yeux et raconte une histoire érotique que tu aurais vécue. À la fin, avoue si c'était vrai ou une invention totale.",
            "DISTANCE : Fais croire à l'autre que tu es en train de te caresser sous ton bureau/table. Si il/elle te croit alors que c'est faux, il/elle doit le faire pour de vrai.",
            "PRÉSENTIEL : Choisis un mot secret. L'autre a 3 questions pour le deviner. Si tu parviens à mentir sans te faire démasquer, tu gagnes un baiser.",
            "WHATSAPP : Envoie une photo d'une partie de ton corps très proche et fais deviner de quoi il s'agit. Si l'autre échoue, il/elle doit te montrer la même zone.",
            "PRÉSENTIEL : Prétends que tu as horreur d'être touché(e) à un endroit précis. L'autre doit tester si c'est un mensonge en te touchant.",
            "DISTANCE : Dis à l'autre que tu as une surprise cachée sur toi. Il/elle doit deviner où. Si il/elle se trompe 3 fois, tu ne lui montres rien du tout.",
            "PRÉSENTIEL : Affirmation : 'Je n'ai jamais fait [action X]'. Si l'autre prouve que tu mens par tes réactions, tu reçois 10 fessées.",
            "WHATSAPP : Envoie un vocal où tu simules un plaisir intense. L'autre doit juger si c'est sincère ou si tu joues la comédie.",
            "PRÉSENTIEL : Fais semblant d'être très timide pendant 2 minutes, puis bascule brusquement dans un comportement dominant.",
            "DISTANCE : Prétends qu'une personne vient d'entrer dans la pièce. Si l'autre panique, il/elle a perdu et doit s'exhiber 5 secondes.",
            "PRÉSENTIEL : Raconte la pire expérience sexuelle que tu n'as JAMAIS eue comme si c'était arrivé. Si l'autre te croit, tu as gagné.",
            "WHATSAPP : Envoie : 'Devine quel objet j'ai hâte d'utiliser sur toi'. Mentir est autorisé pour brouiller les pistes.",
            "PRÉSENTIEL : Lèche une partie de son corps et dis : 'C'est ma préférée'. Mentais-tu ? Si oui, lèche la vraie partie préférée.",
            "DISTANCE : Montre un vêtement à la caméra et dis que tu vas l'enlever. Enlève un autre vêtement à la place sans prévenir.",
            "PRÉSENTIEL : Propose un défi impossible. Si l'autre accepte, avoue que c'était un piège et demande une compensation.",
            "WHATSAPP : Envoie une photo d'un sous-vêtement posé sur ton lit et dis : 'Je viens de l'enlever'. Mensonge ou vérité ?",
            "PRÉSENTIEL : Fais une promesse très cochonne pour plus tard, mais précise que tu es peut-être un(e) grand(e) menteur/euse.",
            "DISTANCE : Regarde l'objectif et dis : 'Je t'aime'. L'autre doit deviner si c'est le jeu ou le cœur qui parle."
        ],
        "F-F": [
            "PRÉSENTIEL : Dis-lui que tu as déjà rêvé d'elle cette nuit. Si elle te croit, elle doit te raconter un de ses rêves sur toi.",
            "WHATSAPP : Envoie-lui : 'Je suis en train de me mouiller à cause de toi'. Elle doit deviner si tu bluffes.",
            "PRÉSENTIEL : Fais semblant d'avoir oublié de mettre une culotte ce soir et laisse-la vérifier.",
            "DISTANCE : Montre-lui un flacon (parfum, huile) et dis que c'est du lubrifiant. Si elle te croit, demande-lui de l'utiliser sur elle.",
            "PRÉSENTIEL : Donne-lui trois indices sur ton fantasme le plus honteux. Un des indices est un mensonge.",
            "WHATSAPP : Envoie une photo de tes lèvres et dis que tu viens d'embrasser quelqu'un d'autre. Vrai ou faux ?",
            "PRÉSENTIEL : Murmure-lui une insulte sexy, puis dis que tu n'as rien dit du tout.",
            "DISTANCE : Fais un strip-tease mais arrête-toi juste avant la fin en prétendant que ta caméra a planté.",
            "PRÉSENTIEL : Propose-lui de choisir entre 'Une vérité brûlante' ou 'Un mensonge excitant'.",
            "WHATSAPP : Envoie une photo de ta main sur ta poitrine et dis que ton cœur bat à 120. Mensonge ?",
            "PRÉSENTIEL : Laisse-la te poser une question intime. Tu as le droit de mentir, mais si elle te démasque, tu finis nue.",
            "DISTANCE : Dis-lui que tu vas te filmer sous la douche, puis envoie une vidéo de toi toute habillée en riant.",
            "PRÉSENTIEL : Fais-lui croire que tu as un tatouage caché dans une zone très privée.",
            "WHATSAPP : Envoie : 'Je préférerais être avec [nom de célébrité] qu'avec toi'. Dis ensuite si c'était un mensonge.",
            "PRÉSENTIEL : Prétends que tu es incapable de résister à ses baisers dans le cou.",
            "DISTANCE : Montre un jouet et dis qu'il est déjà en marche. Elle doit deviner si c'est vrai au son.",
            "PRÉSENTIEL : Dis-lui qu'elle est la meilleure que tu n'aies jamais eue. Mensonge de courtoisie ou vérité ?",
            "WHATSAPP : Envoie une photo de ton lit défait en disant que tu n'es pas seule.",
            "PRÉSENTIEL : Fais semblant de pleurer de plaisir, puis souris-lui sournoisement.",
            "DISTANCE : Dis-lui de fermer les yeux, fais un bruit de vêtement qui tombe, mais ne change rien."
        ],
        "G-G": [
            "PRÉSENTIEL : Raconte-lui une prouesse physique incroyable que tu aurais faite. S'il te croit, il doit essayer de faire mieux.",
            "DISTANCE : Dis-lui que tu es déjà en érection. S'il ne te croit pas, tu dois lui prouver en photo.",
            "PRÉSENTIEL : Fais semblant d'avoir mal quand il te donne une fessée pour qu'il s'arrête, puis demande-en une plus forte.",
            "WHATSAPP : Envoie : 'Je viens de voir une photo de toi et ça m'a rendu fou'. Dis-lui plus tard si c'était vrai.",
            "PRÉSENTIEL : Dis-lui que tu as parié avec un ami que tu finirais au lit avec lui ce soir.",
            "DISTANCE : Prétends que tu es en train de regarder un film porno en même temps que tu lui parles.",
            "PRÉSENTIEL : Propose un duel de regards. Le premier qui rit ou qui détourne les yeux avoue son plus gros mensonge.",
            "WHATSAPP : Envoie une photo de ton torse avec du rouge à lèvres dessus et dis que c'est une marque de bagarre.",
            "PRÉSENTIEL : Dis-lui que tu détestes quand il te domine, tout en agissant de façon très soumise.",
            "WHATSAPP : Envoie : 'Je n'ai jamais eu de fantasme avec un homme avant toi'. Mensonge ou vérité ?",
            "PRÉSENTIEL : Fais-lui croire que tu as un piercing secret que tu ne lui as pas montré.",
            "DISTANCE : Dis-lui que tu vas te déshabiller si il fait 10 pompes. S'il les fait, dis que tu as menti... ou pas.",
            "PRÉSENTIEL : Raconte une anecdote sur ton ex et laisse-le deviner si c'est toi qui as inventé les détails sales.",
            "WHATSAPP : Envoie un selfie avec un air très sérieux et dis : 'Je pense qu'on devrait arrêter'. Rigole 1 min après.",
            "PRÉSENTIEL : Pince son bras et dis que c'était un accident. Recommence en souriant.",
            "DISTANCE : Montre ton caleçon et dis que c'est celui de ton colocataire par erreur.",
            "PRÉSENTIEL : Dis-lui qu'il est beaucoup plus musclé en vrai qu'en photo. Flatte-le pour obtenir une faveur.",
            "WHATSAPP : Envoie : 'Devine ce que je tiens dans ma main gauche'. Si il perd, il finit torse nu.",
            "PRÉSENTIEL : Prétends que tu vas partir, puis reviens et plaque-le contre le mur.",
            "DISTANCE : Dis-lui que tu as enregistré l'audio de ses gémissements."
        ]
    }
    
    return defis.get(mode, defis["Mixte"])