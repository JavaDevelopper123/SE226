from abc import ABC, abstractmethod

weirdWords = "bebops becked becket beckon beclog become bedbug bedded bedder bedeck bedell bedels bedews bedims bedrid bedrug bedsit beduin bedumb beebee beechy beefed beeped beeper beetle beeves beezer befell befits befogs befool before befoul befret begets begged begins begird begirt begone begrim begulf begums beheld behest behind behold behoof behove behowl beiges beigne beings bekiss beknot belfry belied belief belier belies belike belive belled belles bellow belong belons belows belted belter bemire bemist bemixt bemock bemuse bended bendee bender bendys benign bennes bennet bennis bentos benumb benzin benzol benzyl bereft berets berime berlin bermed bermes berths beryls beseem besets beside besmut besnow besoms besots bested bestir bestow bestud betels bethel betide betime betise betons betony betook betted better bettor bevels bevies bevors beweep bewept bewigs beworm beylic beylik beyond bezels bezils bhoots bibbed bibber bibles biceps bicker bicorn bicron bidden energy enface engage engild engine engird engirt englut engram engulf enigma enisle enlace enlist enmesh enmity ennead ennuis ennuye enrage enrapt enrich enserf ensign ensile ensued ensues ensure entail entera enters entice entire entity entrap entree enured enures envied envier envies enwind enwrap enzyme enzyms epacts eparch ephahs ephebe ephebi epical epimer equals equate equids equine equips equity erased eraser erases erbium erects ergate ericas ermine errand errant errata erring ersatz eructs erupts ervils escape escarp escars eschar eschew eskars eskers espial espied espies esprit essays estate esteem esters estral estray estrin estrum estrus etamin etapes etched etcher etches eterne ethane ethene ethers ethics ethnic ethyls ethyne etudes etwees euchre eunuch eupnea eureka euripi eutaxy evaded evader evades evened evener evenly events everts evicts eviler evilly evince evited evites evulse exacta exacts exalts examen exarch exceed excels except excess excide excise excite excuse exedra exempt exequy exerts exeunt exhale exhume exiled exiler exiles exilic exines exists exited expand expats expect expels expend expert expire expiry exsect exsert extant extend extent extern extras exuded exudes exults exurbs exuvia eyases eyebar eyecup eyeful eyeing eyelet eyelid eyries fabber fabled jabber jabiru jabots jacals jacana jackal jacked jacker jacket jading jadish jaeger jagers jagged jagger jagras jaguar jailed jailer jailor jalaps jalops jalopy jambed jambes jammed jammer jangle jangly japans japers japery japing jarful jargon jarina jarrah jarred jarvey jasmin jasper jassid jauked jaunce jaunts jaunty jauped jawans jawing jaygee jayvee jazzbo jazzed jazzer jazzes jeaned jebels jeeing jeeped jeered jeerer jehads jejuna jejune jelled jellos jennet jerboa jereed jerids jerked jerker jerkin jerrid jersey jessed jesses jested jester jesuit jetlag jetons jetsam jetsom jetted jetton jetway jewels jewing jezail jibbed jibber jibers jibing jicama jigged jigger jiggle jiggly jigsaw jihads jilted jilter jiminy jimmie jimper jimply jingal jingko jingle jingly jinked jinker jinnee jinnis jitney jitter jivers jivier jiving jnanas jobbed jobber jockey jockos jocose jocund jogged jogger joggle johnny joined joiner joints joists jojoba jokers jokier jokily joking jolted jolter jorams jordan jorums joseph joshed josher joshes josses jostle jotted jotter jouals jouked joules jounce jouncy journo jousts jovial jowars jowing jowled joyful joying joyous joypop jubbah jubhah jubile judder judged judger judges judoka jugate jugful jugged juggle jugula jugums juiced juicer juices jujube juking juleps jumbal jumble jumbos jumped jumper juncos jungle jungly junior junked junker"

class AbstractCount(ABC):
    def __init__(self, address):
        self.address = address

    @abstractmethod
    def calculateFreqs(self):
        pass

class ListCount(AbstractCount):
    def calculateFreqs(self):
        with open(self.address, 'r') as f:
            text = f.read()
        freqs = []
        for char in set(text):
            if char.isalpha():
                freqs.append((char, text.count(char)))
        freqs.sort(key=lambda x: x[0])
        for char, count in freqs:
            print(f"{char} = {count}")

class DictCount(AbstractCount):
    def calculateFreqs(self):
        with open(self.address, 'r') as f:
            text = f.read()
        freqs = {}
        for char in set(text):
            if char.isalpha():
                freqs[char] = text.count(char)
        for char in sorted(freqs.keys()):
            print(f"{char} = {freqs[char]}")

list_count = ListCount('weirdWords.txt')
list_count.calculateFreqs()

dict_count = DictCount('weirdWords.txt')
dict_count.calculateFreqs()
