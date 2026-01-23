import streamlit as st
import random, pandas as pd, time, firebase_admin, string
from firebase_admin import credentials, firestore
from streamlit_gsheets import GSheetsConnection
DEFIS_BACKUP = {
    "audacieux": {
        "Mixte": [
            "Retire un vêtement de ton choix.", "Fais une proposition indécente à l'autre.", 
            "Laisse l'autre te bander les yeux.", "Embrasse l'endroit le plus sensible de l'autre.",
            "Danse de façon provocante 1 min.", "Prends une photo osée et montre-la.",
            "Demande un ordre difficile.", "Fais un suçon discret.",
            "Pratique un effeuillage lent.", "Dis ta partie préférée de son corps."
        ],
        "F-F": [
            "Caresse sa nuque avec audace.", "Murmure un désir interdit entre femmes.",
            "Trace une ligne imaginaire avec tes lèvres de son cou à sa poitrine.",
            "Demande-lui de te plaquer contre le mur.", "Enlève ton soutien-gorge sans retirer ton haut.",
            "Fais-la rougir avec une confidence crue.", "Prends ses mains et place-les là où tu veux être touchée.",
            "Lèche ton doigt et effleure son oreille.", "Propose un jeu de rôle spontané.", "Dis-lui quel sous-vêtement elle devrait porter pour t'exciter."
        ],
        "G-G": [
            "Montre ta force en le soulevant.", "Donne-lui un ordre provocant.",
            "Plaque-le fermement et fixe son regard.", "Défais sa ceinture avec tes dents.",
            "Mords son cou jusqu'à laisser une marque.", "Impose tes mains sur son torse.",
            "Demande-lui de te porter jusqu'au lit/canapé.", "Défie-le au bras de fer : le perdant retire un vêtement.",
            "Prends le contrôle total de ses mouvements.", "Dis-lui ce que tu vas lui faire subir plus tard."
        ]
    },
    "coquin": {
        "Mixte": ["Lèche tes lèvres en le fixant.", "Mords ton doigt sensuellement.", "Envoie un SMS sexy.", "Caresse l'intérieur de sa cuisse.", "Fais une pose suggestive.", "Murmure un secret impur.", "Joue avec la bretelle de ton vêtement.", "Souffle dans son cou.", "Regarde-le avec envie.", "Effleure son entrejambe par-dessus les vêtements."],
        "F-F": ["Mords son lobe d'oreille.", "Effleure son décolleté.", "Fais-lui un clin d'œil incendiaire.", "Caresse ses hanches lentement.", "Dis-lui que ses mains sont magiques.", "Siffle-lui une envie à l'oreille.", "Lèche ton pouce et frotte ses lèvres.", "Masse son bas du dos.", "Demande-lui un baiser 'papillon'.", "Fais vibrer ton téléphone contre sa peau."],
        "G-G": ["Caresse ses muscles fermement.", "Mords son épaule.", "Glisse ta main dans sa poche arrière.", "Fais une remarque sur son anatomie.", "Tire-le vers toi par le col.", "Souffle sur son torse nu.", "Lèche tes lèvres en regardant son bas-ventre.", "Frotte ta barbe (ou ton menton) contre son cou.", "Donne-lui une tape taquine sur les fesses.", "Dis-lui : 'Tu es à croquer'."]
    },
    "dominant": {
        "Mixte": ["Ordonne-lui de se taire.", "Choisis sa position.", "Exige un compliment.", "Donne une fessée.", "Interdis-lui de bouger.", "Guide ses mains.", "Demande une boisson à genoux.", "Impose un rythme.", "Fais-lui fermer les yeux.", "Décide du prochain retrait de vêtement."],
        "F-F": ["Force-la à te regarder.", "Exige qu'elle t'embrasse la main.", "Dis-lui de se déshabiller sous tes yeux.", "Contrôle sa respiration en la tenant par le menton.", "Donne-lui un défi immédiat.", "Ordonne-lui de te faire un massage.", "Fais-la attendre ton baiser.", "Demande-lui de te décrire comme sa reine.", "Tire-la par les cheveux (doucement).", "Prends sa place sur le siège."],
        "G-G": ["Plaque-le contre le mur.", "Donne un ordre ferme.", "Prends le contrôle de sa tête.", "Dis-lui de se mettre à tes pieds.", "Exige qu'il retire son haut.", "Utilise-le comme ton trône.", "Force-le à demander la permission.", "Mords-le là où tu veux marquer ton territoire.", "Fais-le reculer jusqu'à ce qu'il soit bloqué.", "Rappelle-lui qui commande ici."]
    },
    "esclave": {
        "Mixte": ["Demande pardon à genoux.", "Masse ses pieds.", "Appelle-le Maître/Maîtresse.", "Obéis au doigt et à l'oeil.", "Demande la permission pour parler.", "Embrasse ses chaussures.", "Reste prostré(e).", "Laisse l'autre te manipuler.", "Subis une fessée sans bouger.", "Fais une déclaration de soumission."],
        "F-F": ["Sers-la comme une reine.", "Embrasse ses pieds.", "Demande la permission de la toucher.", "Réalise son moindre désir pendant 2 min.", "Appelle-la 'Maîtresse'.", "Laisse-la te bander les yeux.", "Masse ses jambes en restant au sol.", "Suis-la partout dans la pièce.", "Laisse-la choisir ton châtiment.", "Dis pourquoi tu aimes lui obéir."],
        "G-G": ["Appelle-le 'Maître'.", "Reste aux pieds de son fauteuil.", "Laisse-le utiliser ton corps comme il veut.", "Nettoie une partie de son corps avec ta langue.", "Demande humblement une caresse.", "Porte ses affaires sans rouspéter.", "Accepte d'être son jouet.", "Décris ta joie de le servir.", "Laisse-le te dominer physiquement.", "N'agis que sur son ordre."]
    },
    "exhibionniste": {
        "Mixte": ["Soulève ton haut 10s.", "Reste nu(e) face à la fenêtre.", "Prends une photo érotique.", "Fais une pose de mannequin.", "Baisse ton bas au maximum.", "Simule un acte seule.", "Montre tes sous-vêtements.", "Marche de façon provocante.", "Raconte ta fois où tu as été vu(e).", "Laisse l'autre te filmer (10s)."],
        "F-F": ["Montre tes courbes avec fierté.", "Pose sans rien devant le miroir avec elle.", "Danse de façon lascive.", "Ouvre ta chemise lentement.", "Laisse-la admirer ta poitrine.", "Fais une cambrure extrême.", "Reste en sous-vêtements tout le tour.", "Prends un selfie de tes fesses.", "Décris ce que ça te fait d'être regardée.", "Touche-toi sensuellement devant elle."],
        "G-G": ["Contracte tes muscles.", "Baisse ton pantalon.", "Reste torse nu.", "Montre ton anatomie.", "Fais une pose de force.", "Raconte ton plaisir d'être maté.", "Prends une photo de ton bas-ventre.", "Marche nu devant lui.", "Laisse-le te regarder sous tous les angles.", "Fais jouer tes pectoraux."]
    },
    "gourmand": {
        "Mixte": ["Lèche sa peau.", "Nourris-le.", "Goûte son cou.", "Mords ses lèvres.", "Lèche tes doigts.", "Utilise du chocolat/miel.", "Décris son goût.", "Aspire son lobe.", "Lèche ses mains.", "Fais passer un glaçon sur lui."],
        "F-F": ["Goûte le parfum de son cou.", "Mange un fruit sensuellement.", "Lèche sa clavicule.", "Mords doucement ses lèvres.", "Savourer sa peau comme un dessert.", "Utilise du gloss et embrasse-la.", "Lèche sa paume.", "Décris la douceur de son goût.", "Fais semblant de la dévorer.", "Lèche tes lèvres après l'avoir embrassée."],
        "G-G": ["Lèche son torse.", "Mords son cou vigoureusement.", "Lèche la sueur (ou l'eau) sur sa peau.", "Goute ses lèvres fermement.", "Nourris-le brutalement.", "Lèche son oreille.", "Mords son avant-bras.", "Passe ta langue sur ses abdos.", "Lèche son pouce.", "Dis quel goût il a pour toi."]
    },
    "intello": {
        "Mixte": ["Explique un fantasme complexe.", "Analyse son regard.", "Récite un poème.", "Utilise 5 mots savants.", "Parle de psychologie érotique.", "Cite un auteur.", "Invente une énigme.", "Debat sur le plaisir.", "Apprends-lui un mot étranger.", "Décris son aura."],
        "F-F": ["Récite un poème saphique.", "Décris sa beauté avec philosophie.", "Analyse le lien entre vos esprits.", "Parle de la sensualité féminine historique.", "Utilise des métaphores florales.", "Lis-lui un passage érotique.", "Explique pourquoi l'intelligence t'excite chez elle.", "Anatomie du désir féminin : fais un cours.", "Décris ton fantasme le plus cérébral.", "Compare-la à une déesse grecque."],
        "G-G": ["Parle de l'histoire du désir masculin.", "Cite un auteur gai célèbre.", "Analyse la virilité de l'autre.", "Debat sur le pouvoir et le sexe.", "Utilise des termes techniques pour le corps.", "Raconte un mythe grec sur deux hommes.", "Explique la science de l'excitation.", "Décris sa structure musculaire avec précision.", "Fais une liste de livres inspirants.", "Parle de la tension entre vos deux esprits."]
    },
    "menteur": {
        "Mixte": ["Raconte un faux fantasme.", "Prétends un secret.", "Simule une émotion.", "Fais une promesse bidon.", "Mime une envie fausse.", "Invente une anecdote.", "Dis un mensonge crédible.", "Joue un rôle.", "Cache un objet imaginaire.", "Fais-lui deviner le vrai du faux."],
        "F-F": ["Dis-lui que tu ne portes pas de culotte (vrai ou faux ?).", "Raconte une rencontre féminine imaginaire.", "Prétends que tu as une surprise pour elle.", "Fais-lui croire que tu as entendu un bruit.", "Mime un plaisir simulé.", "Dis-lui que tu as déjà fait ça avec une autre.", "Joue l'indifférente alors que tu es excitée.", "Invente un nom secret pour elle.", "Fais semblant d'être fâchée pour un baiser.", "Raconte un rêve érotique inventé."],
        "G-G": ["Raconte une prouesse imaginaire.", "Prétends que tu as un avantage sur lui.", "Fais-lui croire à un nouveau défi.", "Invente une règle au jeu.", "Dis que tu as vu quelque chose sur son téléphone.", "Raconte un faux exploit sportif/sexuel.", "Joue le mec soumis alors que tu ne l'es pas.", "Fais semblant d'être fatigué pour le surprendre.", "Dis un mensonge sur ton passé.", "Mime une douleur pour qu'il te masse."]
    },
    "pervers": {
        "Mixte": ["Décris une pratique taboue.", "Utilise un objet inhabituel.", "Parle de plan à trois.", "Caresse-le avec tes dents.", "Raconte ton souvenir le plus sale.", "Dis ce que tu ferais à un inconnu.", "Utilise un langage cru.", "Regarde une image osée ensemble.", "Fais une caresse interdite.", "Demande sa pensée la plus sale."],
        "F-F": ["Propose un jeu de rôle féminin osé.", "Caresse-la avec tes cheveux.", "Décris ton envie d'être vue avec une autre femme.", "Utilise un accessoire de mode pour la caresser.", "Parle de ton attirance pour ses zones interdites.", "Lèche une zone non sexuelle de façon érotique.", "Décris un fantasme de soumission totale.", "Enlève ta culotte et donne-la lui.", "Propose de la regarder faire seule.", "Murmure des mots très vulgaires."],
        "G-G": ["Sois cru dans tes paroles.", "Décris une scène de groupe masculine.", "Utilise ta ceinture pour le lier.", "Mords-lui les fesses violemment.", "Parle de tes envies les plus animales.", "Pousse-le à bout avec des mots sales.", "Caresse son entrejambe sans t'arrêter.", "Propose un défi de résistance sexuelle.", "Décris comment tu veux le 'marquer'.", "Dis-lui ce que tu ferais s'il était ton prisonnier."]
    },
    "provocateur": {
        "Mixte": ["Défie-le de ne pas te toucher.", "Joue avec tes vêtements.", "Lèche ton doigt.", "Fais une remarque sur son envie.", "Soulève ton bas lentement.", "Regarde-le de haut.", "Reste très proche sans contact.", "Enlève un vêtement à lui.", "Vante tes talents.", "Fais un clin d'oeil incendiaire."],
        "F-F": ["Croise les jambes de façon suggestive.", "Lèche ton doigt en la fixant.", "Joue avec tes cheveux en la regardant.", "Mords ta lèvre inférieure lentement.", "Dis-lui : 'Je sais que tu me veux'.", "Effleure sa poitrine du bout des ongles.", "Fais-la attendre pour un baiser.", "Déboutonne un bouton de ton chemisier.", "Mets tes mains derrière ta tête.", "Dis-lui : 'Regarde ce que tu ne peux pas toucher'."],
        "G-G": ["Rapproche ton visage du sien sans toucher.", "Vante tes talents au lit.", "Contraction musculaire provocante.", "Marche devant lui en accentuant tes mouvements.", "Dis-lui qu'il est trop faible pour résister.", "Mets ta main sur sa cuisse et retire-la vite.", "Défie-le du regard.", "Lèche ton pouce et frotte son cou.", "Siffle quand il se déplace.", "Dis-lui : 'T'as pas de couilles si tu ne m'embrasses pas'."]
    },
    "romantique": {
        "Mixte": ["Danse un slow.", "Dis pourquoi tu l'aimes.", "Embrasse son front.", "Tiens ses mains.", "Raconte votre premier baiser.", "Fais un massage doux.", "Regarde-le avec tendresse.", "Fais-lui un câlin long.", "Écris un mot d'amour.", "Caresse son visage."],
        "F-F": ["Embrasse ses paupières doucement.", "Tiens-lui la main longuement.", "Fais-lui un compliment sur son âme.", "Brosse ses cheveux avec tes doigts.", "Dis-lui ce que tu as ressenti la première fois.", "Fais un massage des mains lent.", "Regarde-la dans les yeux en souriant.", "Murmure un 'je t'aime' sincère.", "Caresse son visage avec le dos de ta main.", "Enlace-la par la taille."],
        "G-G": ["Caresse son visage avec tendresse.", "Fais-lui un câlin de 30 secondes.", "Dis-lui ce que tu admires chez lui.", "Pose ta tête sur son épaule.", "Regarde-le droit dans les yeux.", "Raconte un souvenir fort entre vous.", "Tiens sa main fermement.", "Embrasse sa tempe.", "Fais-lui un compliment sur sa présence.", "Masse son cou doucement."]
    },
    "salope": {
        "Mixte": ["Mets-toi à quatre pattes.", "Demande à être traité(e) rudement.", "Dis des mots vulgaires.", "Supplie pour une caresse.", "Propose une vidéo courte.", "Montre ta soumission totale.", "Exige une fessée.", "Dis à quel point tu es facile.", "Demande à être utilisé(e).", "Décris ta perversité."],
        "F-F": ["Dis-lui à quel point tu es facile pour elle.", "Exige d'être sa chose.", "Écarte les jambes devant elle.", "Demande-lui de te donner un nom vulgaire.", "Dis-lui que tu veux être dévorée.", "Lèche ses chaussures.", "Prends une position humiliante mais excitante.", "Supplie-la de te posséder.", "Dis-lui : 'Fais de moi ta pute'.", "Offre-lui ton corps sans condition."],
        "G-G": ["Supplie-le de te posséder.", "Utilise des mots vulgaires.", "Mets-toi à genoux.", "Demande-lui de te traiter comme une merde.", "Propose-lui de te baiser maintenant.", "Dis-lui que tu es son trou.", "Exige qu'il te donne des ordres sales.", "Décris ton envie d'être pris violemment.", "Lèche son entrejambe par-dessus le tissu.", "Dis-lui : 'Je suis ta salope'."]
    },
    "soumis": {
        "Mixte": ["Demande la permission.", "Baisse les yeux.", "Masse ses pieds.", "Laisse-le décider.", "Dis 'Oui Maître/Maîtresse'.", "Reste immobile.", "Demande un châtiment.", "Réalise un voeu.", "Sers-le/la.", "Dis pourquoi tu obéis."],
        "F-F": ["Laisse-la choisir tes sous-vêtements.", "Obéis à son moindre geste.", "Baisse la tête quand elle te parle.", "Reste à ses pieds.", "Demande la permission de la toucher.", "Laisse-la te guider partout.", "Dis 'Oui ma Reine'.", "Masse ses jambes en silence.", "N'agis que si elle te le demande.", "Remercie-la après chaque ordre."],
        "G-G": ["Reste immobile pendant ses caresses.", "Dis 'Oui mon Maître'.", "Accepte n'importe quelle fessée.", "Laisse-le te dominer au sol.", "Suis ses instructions à la lettre.", "Demande pardon pour rien.", "Fais ce qu'il te dit sans discuter.", "Reste à genoux.", "Dis-lui qu'il est ton seul chef.", "Laisse-le te manipuler."]
    },
    "souple": {
        "Mixte": ["Touche tes pieds.", "Cambre-toi.", "Position acrobatique.", "Grand écart partiel.", "Lève une jambe.", "Pont ou torsion.", "Étirement suggestif.", "Enlace l'autre.", "Masse avec souplesse.", "Fais le chat."],
        "F-F": ["Enlace tes jambes autour d'elle.", "Fais un étirement suggestif.", "Montre ta cambrure au miroir.", "Plie-toi en deux devant elle.", "Lève ta jambe sur son épaule.", "Fais une torsion sensuelle.", "Masse-la en restant très souple.", "Montre ta flexibilité au sol.", "Glisse sous ses jambes.", "Fais une pose de yoga érotique."],
        "G-G": ["Montre une position acrobatique.", "Soulève-le avec tes jambes.", "Fais le pont au-dessus de lui.", "Touche tes pieds sans plier les genoux.", "Montre ta souplesse dorsale.", "Caresse-le en restant cambré.", "Fais une démonstration de flexibilité.", "Mets tes jambes derrière ta tête (si possible).", "Fais un étirement des bras derrière le dos.", "Mouvements de hanches fluides."]
    },
    "sournois": {
        "Mixte": ["Baiser surprise.", "Chatouille-le.", "Défais un bouton.", "Cache un glaçon.", "Caresse interdite.", "Vole un objet.", "Mime un faux secret.", "Pince-lui les fesses.", "Fais-lui peur sexy.", "Chuchote une bêtise."],
        "F-F": ["Défais discrètement son agrafe.", "Glisse ta main là où c'est interdit.", "Vole-lui un baiser dans le cou.", "Pince-lui la hanche en traître.", "Surprends-la avec une main froide.", "Déboutonne ton haut en cachette.", "Regarde-la via un reflet.", "Glisse un mot coquin dans sa poche.", "Chatouille son entrejambe.", "Fais semblant de chercher quelque chose sur elle."],
        "G-G": ["Surprends-le par une caresse basse.", "Pince-lui les fesses en secret.", "Défais sa braguette discrètement.", "Mords-lui l'oreille par surprise.", "Vole son téléphone et demande un baiser.", "Fais-lui un croche-patte pour qu'il tombe sur toi.", "Lèche son cou quand il ne regarde pas.", "Glisse ta main sous son tee-shirt.", "Fais-lui une remarque taquine.", "Cache-toi et saute-lui dessus."]
    },
    "sportif": {
        "Mixte": ["5 pompes au-dessus de lui.", "Porte-le.", "Gainage sensuel.", "Masse ses muscles.", "Bras de fer coquin.", "Montre tes abdos.", "Squats suggestifs.", "Fais monter le cardio.", "Utilise ta force.", "Transpire un peu."],
        "F-F": ["Fais du gainage pendant qu'elle te caresse.", "Masse ses muscles fermement.", "Porte-la dans tes bras.", "Fais des squats en la fixant.", "Montre-lui tes jambes toniques.", "Défie-la à un jeu de force.", "Fais des étirements dynamiques.", "Contrôle ton souffle de façon bruyante.", "Masse son dos vigoureusement.", "Fais des abdos et embrasse-la à chaque remontée."],
        "G-G": ["Fais un bras de fer coquin.", "Montre ta puissance physique.", "Fais des pompes claquées.", "Soulève-le de terre.", "Contracte tes muscles devant lui.", "Défie-le à un combat de lutte.", "Porte-le sur tes épaules.", "Masse ses trapèzes.", "Fais du gainage face à lui.", "Utilise ta force pour le maintenir."]
    },
    "tendance_lesbienne": {
        "Mixte": ["Parle de ton attirance femmes.", "Caresse-le comme une femme.", "Décris une peau féminine.", "Dis un fantasme lesbien.", "Mime une scène saphique.", "Demande-lui de jouer la femme.", "Explique ta curiosité.", "Caresse ses seins/torse.", "Dis un nom de femme sexy.", "Imagine-toi avec une autre."],
        "F-F": ["Masse sa poitrine avec lenteur.", "Explore sa féminité avec douceur.", "Lèche ses doigts un par un.", "Murmure-lui : 'Rien ne vaut une femme'.", "Caresse ses courbes longuement.", "Décris ce que tu aimes dans son corps de femme.", "Embrasse l'intérieur de sa cuisse.", "Respire son parfum féminin.", "Fais-lui une déclaration saphique.", "Laisse tes mains se perdre sur elle."],
        "G-G": ["(Inactif - Transformé en Tendance Virile)", "Masse son torse fermement.", "Dis ce que tu aimes chez les hommes.", "Caresse ses muscles.", "Embrasse son cou vigoureusement.", "Regarde-le comme un mâle.", "Complimente sa virilité.", "Décris sa force.", "Mords son avant-bras.", "Dis : 'J'aime ton corps d'homme'."]
    },
    "timide": {
        "Mixte": ["Avoue une honte.", "Embrasse timidement.", "Rougis.", "Cache ton visage.", "Caresse hésitante.", "Dis un secret.", "Laisse-le faire.", "Éteins la lumière.", "Baiser papillon.", "Dis 'Tu m'intimides'."],
        "F-F": ["Rougis sous son regard.", "Cache ton visage dans son cou.", "Embrasse-la sur la joue seulement.", "Dis-lui que tu n'oses pas.", "Laisse-la prendre tes mains.", "Regarde tes pieds en lui parlant.", "Fais une caresse très légère.", "Murmure une envie sans la regarder.", "Demande-lui de te guider.", "Ferme les yeux pour l'embrasser."],
        "G-G": ["Évite son regard en souriant.", "Caresse sa main avec hésitation.", "Dis-lui qu'il t'intimide.", "Baisse la tête quand il s'approche.", "Fais un baiser rapide.", "Avoue que tu es nerveux.", "Laisse-le prendre l'initiative.", "Dis-lui qu'il est trop beau pour toi.", "Cache ton visage contre son torse.", "Demande-lui d'être doux."]
    },
    "voyeur": {
        "Mixte": ["Regarde-le se déshabiller.", "Observe via un miroir.", "Fixe son entrejambe.", "Demande une pose.", "Regarde-le se caresser.", "Décris ce que tu vois.", "Utilise ton téléphone.", "Regarde par un trou.", "Ne touche pas, regarde.", "Analyse son excitation."],
        "F-F": ["Demande-lui de poser pour toi.", "Regarde-la se caresser 30s.", "Observe ses mouvements de hanches.", "Fixe sa poitrine sans cligner.", "Décris chaque détail de son corps nu.", "Regarde-la s'habiller lentement.", "Demande-lui de montrer sa lingerie.", "Observe son visage pendant qu'elle a du plaisir.", "Mets-la sous la lumière et regarde-la.", "Dis-lui : 'J'adore te regarder'."],
        "G-G": ["Fixe ses parties intimes.", "Demande-lui de faire un mouvement sexy.", "Regarde ses muscles travailler.", "Observe-le sous la douche (ou imagine).", "Demande-lui de se mettre à poil.", "Fixe son regard pendant qu'il se touche.", "Décris sa virilité à voix haute.", "Regarde son dos quand il marche.", "Observe ses veines et sa peau.", "Dis : 'T'es un spectacle pour mes yeux'."]
    },
    "sauvage": {
        "Mixte": ["Mords-le.", "Griffe son dos.", "Attrape ses cheveux.", "Baiser brutal.", "Rugis.", "Déchire un truc (vieux).", "Plaque-le.", "Lutte avec lui.", "Caresse intense.", "Sois animal."],
        "F-F": ["Attrape-la par les cheveux pour un baiser.", "Sois intense et brutale.", "Mords-lui le cou sans prévenir.", "Griffe ses hanches.", "Plaque-la sur le lit violemment.", "Dévore-la du regard.", "Fais-lui un baiser qui lui coupe le souffle.", "Utilise tes ongles sur sa peau.", "Domine-la physiquement.", "Murmure des mots sauvages."],
        "G-G": ["Lutte au sol avec lui.", "Plaque-le fermement au lit.", "Mords son épaule jusqu'à la marque.", "Attrape ses mains et bloque-les.", "Donne-lui une fessée qui claque.", "Respire fort contre son cou.", "Sois brutal dans tes caresses.", "Tire-le par les cheveux.", "Montre-lui ton côté animal.", "Pousse-le contre le mur."]
    }
}
# --- CONFIGURATION ---
TRAITS_DISPO = ["pervers", "salope", "provocateur", "exhibionniste", "tendance_lesbie", "audacieux", "soumis", "dominant", "souple", "sportif", "timide", "coquin", "voyeur", "romantique", "esclave", "gourmand", "intello", "sournois", "menteur"]

st.set_page_config(page_title="Stream Pulse", page_icon="👿", layout="wide")

# --- AUDIO & STYLE PREMIUM ---
SOUND_NOTIF = "https://www.soundjay.com/buttons/sounds/button-3.mp3"
SOUND_MODIF = "https://www.soundjay.com/buttons/sounds/beep-07a.mp3"
SOUND_VALID = "https://www.soundjay.com/misc/sounds/bell-ringing-05.mp3"

st.markdown(f"""
    <style>
    .stApp {{ background: linear-gradient(135deg, #121212 0%, #1a1a2e 100%); color: #e0e0e0; }}
    div.stButton > button:first-child {{ 
        background: linear-gradient(90deg, #ff4b2b 0%, #ff416c 100%); 
        color: white; border-radius: 15px; font-weight: bold; border: none; height: 3.5em; width: 100%;
    }}
    .score-box {{ background: rgba(0, 0, 0, 0.4); border: 2px solid #ff416c; border-radius: 15px; padding: 15px; text-align: center; color: #ff416c; font-weight: 800; font-size: 22px; margin-bottom: 10px; }}
    .stAlert {{ background: rgba(255, 255, 255, 0.05) !important; backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.1) !important; color: white !important; }}
    .alert-modif {{ background-color: rgba(255, 193, 7, 0.2); color: #ffc107; padding: 10px; border-radius: 10px; border: 1px solid #ffc107; text-align: center; font-weight: bold; }}
    </style>
    <audio id="notif-sound" src="{SOUND_NOTIF}" preload="auto"></audio>
    <audio id="modif-sound" src="{SOUND_MODIF}" preload="auto"></audio>
    <audio id="valid-sound" src="{SOUND_VALID}" preload="auto"></audio>
""", unsafe_allow_html=True)

# --- CONNEXIONS ---
if not firebase_admin._apps:
    fb_dict = dict(st.secrets["firebase"])
    cred = credentials.Certificate(fb_dict)
    firebase_admin.initialize_app(cred)
db = firestore.client()
conn_sheets = st.connection("gsheets", type=GSheetsConnection)

def obtenir_un_defi(trait, genre_session):
    """
    Choisit un défi au hasard pour un trait donné.
    Priorité 1 : Fichier .py spécifique (ex: pervers.py)
    Priorité 2 : Dictionnaire DEFIS_BACKUP dans main.py
    Priorité 3 : Improvisation libre
    """
    # 1. Nettoyage du nom du trait (ex: "Tendance Lesbienne" -> "tendance_lesbienne")
    trait_clean = trait.lower().strip().replace(" ", "_")
    
    # --- NIVEAU 1 : TENTATIVE DEPUIS LE FICHIER .PY ---
    try:
        # Importation dynamique du module correspondant au trait
        module = importlib.import_module(trait_clean)
        importlib.reload(module)
        
        # Appel de la fonction get_defis(mode) présente dans ton fichier .py
        liste_defis = module.get_defis(genre_session)
        
        if liste_defis and len(liste_defis) > 0:
            # PIOCHE ALÉATOIRE dans le fichier .py
            return random.choice(liste_defis)
        else:
            raise ValueError("Liste vide dans le fichier .py")

    except (ImportError, AttributeError, ValueError):
        # --- NIVEAU 2 : SECOURS VIA LE DICTIONNAIRE DEFIS_BACKUP ---
        # Si le fichier .py n'existe pas ou contient une erreur
        if trait_clean in DEFIS_BACKUP:
            options_trait = DEFIS_BACKUP[trait_clean]
            
            # On récupère la liste correspondant au genre (F-F, G-G ou Mixte)
            # Si le genre spécifique n'existe pas, on prend 'Mixte' par défaut
            liste_secours = options_trait.get(genre_session, options_trait.get("Mixte"))
            
            if liste_secours:
                # PIOCHE ALÉATOIRE dans le dictionnaire de secours
                return random.choice(liste_secours)

        # --- NIVEAU 3 : ULTIME RECOURS (SÉCURITÉ ABSOLUE) ---
        # Si même le backup est introuvable pour ce trait
        return f"Improvisation libre : Réalise une action qui illustre ton trait '{trait}' de manière '{genre_session}'."
        def afficher_jeu(doc_ref):
        # On crée le conteneur principal une seule fois
if 'zone_jeu' not in st.session_state:
    st.session_state.zone_jeu = st.empty()

# Récupération des données
data = doc_ref.get().to_dict()

with st.session_state.zone_jeu.container():
    # 1. TITRE FIXE
    st.markdown("<h2 style='text-align: center;'>🎮 SESSION EN COURS</h2>", unsafe_allow_html=True)

    # 2. GRILLE DES SCORES (IMMOBILE)
    # On définit les colonnes pour que les boîtes aient toujours la même taille
    c1, c2 = st.columns(2)
    
    with c1:
        st.markdown(f"""
            <div style='border: 2px solid #FF4B4B; border-radius: 10px; padding: 15px; text-align: center; height: 100px;'>
                <div style='font-size: 1.2em; font-weight: bold;'>{data['J1_Nom']}</div>
                <div style='font-size: 1.5em; color: #FF4B4B;'>{data['J1_Score']} pts</div>
            </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
            <div style='border: 2px solid #FF4B4B; border-radius: 10px; padding: 15px; text-align: center; height: 100px;'>
                <div style='font-size: 1.2em; font-weight: bold;'>{data['J2_Nom']}</div>
                <div style='font-size: 1.5em; color: #FF4B4B;'>{data['J2_Score']} pts</div>
            </div>
        """, unsafe_allow_html=True)

    st.write("") # Espace fixe

    # 3. ZONE DES DÉFIS (STRUCTURE FIXE)
    d1, d2 = st.columns(2)
    
    with d1:
        # On utilise une hauteur fixe pour que la boîte ne change pas de taille selon le texte
        st.markdown(f"""
            <div style='background-color: #1E1E1E; border-left: 5px solid #FF4B4B; padding: 15px; min-height: 150px;'>
                <small>DÉFI POUR {data['J1_Nom'].upper()}</small><br>
                <p style='font-size: 1.1em;'>{data['J1_Defi']}</p>
            </div>
        """, unsafe_allow_html=True)
        # État de validation simple (texte court pour ne pas décaler)
        statut_j1 = "✅ PRÊT" if data.get('J1_Ready') else "⏳ EN ATTENTE"
        st.caption(statut_j1)

    with d2:
        st.markdown(f"""
            <div style='background-color: #1E1E1E; border-left: 5px solid #FF4B4B; padding: 15px; min-height: 150px;'>
                <small>DÉFI POUR {data['J2_Nom'].upper()}</small><br>
                <p style='font-size: 1.1em;'>{data['J2_Defi']}</p>
            </div>
        """, unsafe_allow_html=True)
        statut_j2 = "✅ PRÊT" if data.get('J2_Ready') else "⏳ EN ATTENTE"
        st.caption(statut_j2)

    st.write("") 

    # 4. ZONE DU BOUTON (POSITION FIXE)
    mon_role = "J1" if st.session_state.nom == data['J1_Nom'] else "J2"
    deja_pret = data.get(f"{mon_role}_Ready", False)

    # Le bouton est toujours là, il change juste d'état (activé/désactivé)
    if not deja_pret:
        if st.button("J'AI FAIT MON DÉFI", use_container_width=True, type="primary", key="btn_val"):
            doc_ref.update({f"{mon_role}_Ready": True})
            st.rerun()
    else:
        st.button("PARTENAIRE EN TRAIN DE JOUER...", use_container_width=True, disabled=True, key="btn_wait")

# 5. LOGIQUE DE PASSAGE AU TOUR SUIVANT (INVISIBLE)
if data.get('J1_Ready') and data.get('J2_Ready'):
    # On prépare le prochain tour en arrière-plan
    nouveau_d1 = obtenir_un_defi(data['J2_Trait'], data['Genre'])
    nouveau_d2 = obtenir_un_defi(data['J1_Trait'], data['Genre'])
    
    doc_ref.update({
        "J1_Defi": nouveau_d1, "J2_Defi": nouveau_d2,
        "J1_Ready": False, "J2_Ready": False,
        "J1_Score": data['J1_Score'] + 1, "J2_Score": data['J2_Score'] + 1
    })
    st.rerun()
# --- LOGIQUE D'ACCUEIL ---
params = st.query_params
room_id = params.get("room")
role_auto = params.get("role")

if "mode" not in st.session_state and not room_id:
    st.title("🔥 Divine Pulse")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🆕 Créer une nouvelle Session"):
            st.session_state.mode = "creation"; st.rerun()
    with col2:
        if st.button("🔌 Se connecter à une Session"):
            st.session_state.mode = "connexion"; st.rerun()
    st.stop()

# --- MODE CRÉATION ---
if st.session_state.get("mode") == "creation":
    st.title("🛡️ Configurer la Session")
    c_name = st.text_input("Nom de la Session (Unique)")
    c_pass = st.text_input("Mot de passe secret", type="password")
    n1 = st.text_input("Ton Prénom")
    s1 = st.radio("Ton Sexe", ["Homme", "Femme"], horizontal=True)
    n2 = st.text_input("Prénom du partenaire")
    traits_b = st.multiselect(f"Personnalité de {n2} :", TRAITS_DISPO)

    if st.button("🚀 Lancer la Session"):
        if c_name and c_pass and n1 and traits_b:
            doc_ref = db.collection("sessions").document(c_name)
            if doc_ref.get().exists:
                st.error("Ce nom de session existe déjà !")
            else:
                doc_ref.set({
                    "pw_session": c_pass, "n1": n1, "s1": s1, "n2": n2,
                    "traits_de_b": traits_b, "step": 1, "update_ts": time.time(), "last_action": "init"
                })
                st.query_params.room = c_name; st.query_params.role = "A"; st.rerun()
    if st.button("⬅️ Retour"): del st.session_state.mode; st.rerun()
    st.stop()

# --- MODE CONNEXION / AUTH ---
if (st.session_state.get("mode") == "connexion" or room_id) and f"auth_done_{room_id}" not in st.session_state:
    st.title("🔌 Accès Privé")
    l_name = st.text_input("Nom de la Session", value=room_id if room_id else "")
    l_pass = st.text_input("Mot de passe", type="password")
    
    if st.button("Se connecter"):
        doc = db.collection("sessions").document(l_name).get()
        if doc.exists:
            data = doc.to_dict()
            if data['pw_session'] == l_pass:
                st.session_state[f"auth_done_{l_name}"] = True
                st.query_params.room = l_name
                if not role_auto:
                    st.session_state.temp_data = data
                    st.session_state.mode = "select_role"
                st.rerun()
            else: st.error("Mot de passe incorrect.")
        else: st.error("Session introuvable.")
    st.stop()

# --- SÉLECTION DU RÔLE ---
if st.session_state.get("mode") == "select_role":
    data = st.session_state.temp_data
    st.subheader(f"Session : {st.query_params.room}")
    role_choice = st.radio("Qui es-tu ?", [data['n1'], data['n2']])
    if st.button("Confirmer mon identité"):
        st.query_params.role = "A" if role_choice == data['n1'] else "B"
        del st.session_state.mode; st.rerun()
    st.stop()

# --- LOGIQUE DE JEU ---
if room_id:
    doc_ref = db.collection("sessions").document(room_id)
    state = doc_ref.get().to_dict()
    role = st.query_params.get("role")

    # ÉTAPE 1 : SETUP B
    if state.get("step") == 1:
        if role == "B":
            st.title(f"💋 Bienvenue {state['n2']}")
            s2 = st.radio("Ton Sexe", ["Homme", "Femme"], horizontal=True)
            traits_a = st.multiselect(f"Comment décrirais-tu {state['n1']} ?", TRAITS_DISPO)
            if st.button("🔥 Commencer le Jeu"):
                genre = "H/H" if state['s1']=="Homme" and s2=="Homme" else "F/F" if state['s1']=="Femme" and s2=="Femme" else "Mixte"
                t_a, t_b = random.choice(traits_a), random.choice(state['traits_de_b'])
                doc_ref.update({
                    "s2": s2, "traits_de_a": traits_a, "genre": genre,
                    "J1_Trait": t_b, "J1_Defi": obtenir_un_defi(t_b, genre), "J1_Score": 0, "J1_Ready": False,
                    "J2_Trait": t_a, "J2_Defi": obtenir_un_defi(t_a, genre), "J2_Score": 0, "J2_Ready": False,
                    "step": 2, "update_ts": time.time(), "last_action": "start"
                })
                st.rerun()
        else:
            st.info(f"⏳ En attente de {state['n2']}...")
            st.code(f"Lien : https://ton-app.streamlit.app/?room={room_id}&role=B")
            time.sleep(4); st.rerun()

    # ÉTAPE 2 : LE JEU
    elif state.get("step") == 2:
        if state.get("J1_Ready") and state.get("J2_Ready"):
            genre = state['genre']
            t_a = random.choice(state['traits_de_a'])
            t_b = random.choice(state['traits_de_b'])
            doc_ref.update({
                "J1_Trait": t_b, "J1_Defi": obtenir_un_defi(t_b, genre), "J1_Score": state['J1_Score']+1, "J1_Ready": False,
                "J2_Trait": t_a, "J2_Defi": obtenir_un_defi(t_a, genre), "J2_Score": state['J2_Score']+1, "J2_Ready": False,
                "update_ts": time.time(), "last_action": "new_round"
            })
            st.rerun()

        # AUDIO SYNC
        if "lts" not in st.session_state: st.session_state.lts = state['update_ts']
        if state['update_ts'] > st.session_state.lts:
            st.session_state.lts = state['update_ts']
            if "jv" not in st.session_state:
                snd = "modif-sound" if state.get("last_action") == "modif" else "notif-sound"
                st.markdown(f'<script>document.getElementById("{snd}").play();</script>', unsafe_allow_html=True)
            else: del st.session_state["jv"]

        st.title(f"⚡ {state['n1']} & {state['n2']}")
        if state.get("last_action") == "modif": st.markdown('<div class="alert-modif">⚠️ Défi modifié par le partenaire !</div>', unsafe_allow_html=True)

        colA, colB = st.columns(2)
        with colA:
            st.markdown(f"<div class='score-box'>{state['n1']} : {state['J1_Score']} pts</div>", unsafe_allow_html=True)
            st.info(f"**DÉFI :**\n\n{state['J1_Defi']}")
            if state.get("J1_Ready"): st.success("✅ Validé")
            elif role == "B":
                if st.button(f"Valider {state['n1']}"):
                    st.session_state["jv"] = True; st.markdown('<script>document.getElementById("valid-sound").play();</script>', unsafe_allow_html=True)
                    doc_ref.update({"J1_Ready": True, "update_ts": time.time(), "last_action": "valid"}); st.rerun()
                with st.expander("✏️ Modifier"):
                    nt = st.text_area("Nouveau texte pour A :")
                    if st.button("Envoyer A"): doc_ref.update({"J1_Defi": nt, "update_ts": time.time(), "last_action": "modif"}); st.rerun()

        with colB:
            st.markdown(f"<div class='score-box'>{state['n2']} : {state['J2_Score']} pts</div>", unsafe_allow_html=True)
            st.warning(f"**DÉFI :**\n\n{state['J2_Defi']}")
            if state.get("J2_Ready"): st.success("✅ Validé")
            elif role == "A":
                if st.button(f"Valider {state['n2']}"):
                    st.session_state["jv"] = True; st.markdown('<script>document.getElementById("valid-sound").play();</script>', unsafe_allow_html=True)
                    doc_ref.update({"J2_Ready": True, "update_ts": time.time(), "last_action": "valid"}); st.rerun()
                with st.expander("✏️ Modifier"):
                    nt = st.text_area("Nouveau texte pour B :")
                    if st.button("Envoyer B"): doc_ref.update({"J2_Defi": nt, "update_ts": time.time(), "last_action": "modif"}); st.rerun()

        if role == "A" and st.sidebar.button("♻️ Reset Salon"): doc_ref.delete(); st.query_params.clear(); st.rerun()
        time.sleep(4); st.rerun()


