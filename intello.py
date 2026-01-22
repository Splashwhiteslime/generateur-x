# intello.py

def get_defis(mode):
    """
    Retourne 20 défis pour le trait Intello.
    Focus : Érotisme verbal, psychologie, fantasmes décrits et stimulation mentale.
    """
    
    defis = {
        "Mixte": [
            "PRÉSENTIEL : Lis à haute voix un passage érotique d'un livre ou d'un site en fixant l'autre à chaque virgule.",
            "WHATSAPP : Envoie une définition de dictionnaire d'un mot impudique et explique pourquoi il te définit ce soir.",
            "PRÉSENTIEL : Explique à l'autre, avec un vocabulaire soutenu et précis, la première chose que tu ferais si vous étiez seuls sur une île.",
            "DISTANCE : Analyse le langage corporel de l'autre face caméra et dis-lui ce que son corps semble réclamer.",
            "PRÉSENTIEL : Cite une phrase célèbre sur l'amour ou le désir, puis détourne-la pour qu'elle devienne très cochonne.",
            "WHATSAPP : Écris un mini-récit de 5 lignes commençant par 'Dans l'obscurité, ma main a glissé...' (Vue Unique).",
            "PRÉSENTIEL : Invente un nouveau mot pour désigner l'excitation que tu ressens en ce moment et explique son étymologie.",
            "DISTANCE : Fais un cours magistral de 30 secondes face caméra sur 'l'art de donner du plaisir'.",
            "PRÉSENTIEL : Demande à l'autre de fermer les yeux et décris-lui une scène érotique si précisément qu'il/elle doit pouvoir l'imaginer.",
            "WHATSAPP : Envoie une énigme coquine. Si l'autre ne trouve pas la réponse en 1 min, il/elle doit enlever un vêtement.",
            "PRÉSENTIEL : Murmure à l'oreille de l'autre trois mots compliqués qui te font de l'effet quand tu penses à lui/elle.",
            "DISTANCE : Montre un livre à la caméra et dis quel personnage de ce livre tu aimerais incarner avec l'autre.",
            "PRÉSENTIEL : Fais une analyse critique (et sexy) de la tenue que porte l'autre en ce moment.",
            "WHATSAPP : Envoie un message codé (en chiffres ou symboles) que l'autre doit déchiffrer pour découvrir ton désir.",
            "PRÉSENTIEL : Propose une joute verbale : le premier qui bégaye ou qui rougit a perdu et doit obéir.",
            "DISTANCE : Explique la théorie de la tension sexuelle face caméra en prenant l'exemple de votre soirée.",
            "PRÉSENTIEL : Dessine une figure géométrique sur la peau de l'autre avec tes lèvres et fais-lui deviner laquelle.",
            "WHATSAPP : Envoie une citation de Freud ou d'un philosophe et explique pourquoi elle justifie tes pulsions ce soir.",
            "PRÉSENTIEL : Demande à l'autre de te raconter son fantasme le plus complexe et analyse-le avec malice.",
            "DISTANCE : Envoie un vocal en utilisant des termes techniques (anatomie) pour décrire ce que tu ressens."
        ],
        "F-F": [
            "PRÉSENTIEL : Décris-lui la texture de sa peau en utilisant uniquement des métaphores littéraires.",
            "WHATSAPP : Envoie-lui un poème de Sappho ou un texte saphique avec une remarque personnelle.",
            "PRÉSENTIEL : Explique-lui pourquoi l'intelligence d'une femme est ton plus grand aphrodisiaque.",
            "DISTANCE : Fais un exposé de 30s sur l'histoire de la lingerie féminine en montrant la tienne.",
            "PRÉSENTIEL : Invente une règle de grammaire coquine que vous devez respecter jusqu'à la fin du jeu.",
            "WHATSAPP : Écris-lui un message secret en utilisant uniquement des emojis pour décrire un acte précis.",
            "PRÉSENTIEL : Regarde-la fixement et devine à quoi elle pense. Si tu as raison, elle doit t'embrasser.",
            "DISTANCE : Lis-lui les paroles d'une chanson sensuelle comme s'il s'agissait d'un texte sacré.",
            "PRÉSENTIEL : Compare ses yeux à deux pierres précieuses et explique comment tu voudrais les sertir sur toi.",
            "WHATSAPP : Envoie une photo de tes lunettes (si tu en as) ou d'un livre posé sur ton ventre nu.",
            "PRÉSENTIEL : Propose-lui un débat sur 'le baiser parfait' et illustre tes arguments par la pratique.",
            "DISTANCE : Envoie un vocal où tu analyses le son de sa respiration quand elle est excitée.",
            "PRÉSENTIEL : Utilise ton index comme un stylo et écris un secret sur son décolleté.",
            "WHATSAPP : Envoie : 'L'esprit est le premier organe sexuel, laisse-moi stimuler le tien'.",
            "PRÉSENTIEL : Décris-lui un tableau célèbre et explique comment vous pourriez reproduire la pose nue.",
            "DISTANCE : Montre-lui un mot compliqué dans un livre et demande-lui de le prononcer de façon sexy.",
            "PRÉSENTIEL : Fais-lui un compliment sur sa structure osseuse (clavicules, hanches) avec un air de prof.",
            "WHATSAPP : Envoie une liste de 3 livres érotiques que vous devriez lire ensemble au lit.",
            "PRÉSENTIEL : Demande-lui de t'enseigner quelque chose, puis distrais-la par des caresses.",
            "DISTANCE : Fais une vidéo de 5s où tu ajustes tes lunettes avec un regard très sombre."
        ],
        "G-G": [
            "PRÉSENTIEL : Utilise un langage architectural pour décrire la musculature de son corps.",
            "DISTANCE : Envoie un message expliquant la chimie du désir (hormones) que tu ressens pour lui.",
            "PRÉSENTIEL : Défie-le sur une question de culture générale. Le perdant doit retirer son caleçon.",
            "WHATSAPP : Envoie une photo de toi en train de lire un livre, torse nu.",
            "PRÉSENTIEL : Explique-lui pourquoi le silence entre vous est plus éloquent que n'importe quelle parole.",
            "DISTANCE : Fais un discours de motivation (style coach) sur pourquoi il doit être ton esclave ce soir.",
            "PRÉSENTIEL : Analyse son odeur et décris les notes (boisées, musquées) comme un œnologue.",
            "WHATSAPP : Envoie un message : 'Ta stratégie de séduction est efficace, mais ma contre-attaque sera plus forte'.",
            "PRÉSENTIEL : Propose de lui donner un cours de massage anatomique en pratiquant sur lui.",
            "DISTANCE : Montre ton visage éclairé par l'écran et explique comment la lumière souligne tes traits.",
            "PRÉSENTIEL : Dis-lui quelle période de l'histoire t'inspire le plus pour vos jeux érotiques.",
            "WHATSAPP : Envoie une citation d'Oscar Wilde ou de Machiavel adaptée à votre jeu.",
            "PRÉSENTIEL : Raconte-lui une anecdote historique sur la séduction tout en le touchant discrètement.",
            "DISTANCE : Décris par message ton processus de pensée quand tu as une érection en le regardant.",
            "PRÉSENTIEL : Regarde-le et dis-lui exactement quel type de dominant ou soumis il ferait selon toi.",
            "WHATSAPP : Envoie : 'La connaissance est le pouvoir, et j'ai hâte de connaître ton corps par cœur'.",
            "PRÉSENTIEL : Utilise un vocabulaire technique pour lui donner des ordres.",
            "DISTANCE : Fais-lui deviner quel vêtement tu as enlevé en lui donnant des indices intellectuels.",
            "PRÉSENTIEL : Propose une partie d'échecs (ou un autre jeu) où chaque pièce prise est un vêtement en moins.",
            "WHATSAPP : Envoie un selfie avec un air de 'professeur sévère' et ordonne-lui d'obéir."
        ]
    }
    
    return defis.get(mode, defis["Mixte"])