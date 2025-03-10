from tkinter import *
from tkinter import messagebox
from math import pi, e, sin, cos, tan, log

window = Tk()
screenSize = "279x442"
window.geometry(screenSize)
window.resizable(0, 0)
window.title("Calcualtor")
#function
def about():
    messagebox.showinfo('About',"\n \n \n   Made by Dinesh Kumar   \n instagram id : @thedineshyadav\n \n")

def clickButton(item):
    global expression
    inputText.set(inputText.get()+(str(item)))

def clearButton():
    global expression
    expression = ""
    inputText.set(inputText.get()[0:-1])

def clearAll():
    inputText.set("")

def expand():
    if screenSize=="279x500":
        window.geometry("279x555")
    else:
        window.geometry("279x555")
def equalButton():
    result = ""
    try:
        result = eval(inputText.get())
        inputText.set(result)
    except:
        result = "ERROR..."
        inputText.set(result)
#menubar
menubar = Menu(window,bg="black",fg="white")
filemenu = Menu(menubar, tearoff=0,bg="black",fg="white")
filemenu.add_command(label="Copy")
filemenu.add_command(label="Paste")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="Edit", menu=filemenu)
helpmenu = Menu(menubar, tearoff=0,bg="black",fg="white")
helpmenu.add_command(label="About", command=about)
menubar.add_cascade(label="Help", menu=helpmenu)

expression = ""
inputText = StringVar()

inputFrame = Frame(window, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="gray",
                    highlightthickness=2)
inputFrame.pack(side=TOP)
inputField = Entry(inputFrame, font=('arial', 25, ), textvariable=inputText, width=50,fg="white", bg="black", bd=0,
                    justify=RIGHT)
inputField.grid(row=0, column=0)
inputField.pack(ipady=13)

mainFrame = Frame(window, width=312, height=272.5, bg="black")
mainFrame.pack()

ac = PhotoImage(file = r"images\ac.png")
acimage = ac.subsample(4,4)
ac = Button(mainFrame, text="AC", fg="black", image=acimage, bd=0, bg="black", cursor="hand2",
               command=lambda: clearAll()).grid(row=0, column=0, padx=1, pady=1)

clear = PhotoImage(file = r"images\clear.png")
clearimage = clear.subsample(4,4)
clear = Button(mainFrame, text="AC", fg="black", image=clearimage, bd=0, bg="black", cursor="hand2",
               command=lambda: clearButton()).grid(row=0, column=1, padx=1, pady=1)

expan_btn = PhotoImage(file = r"images\expan_btn.png")
expan_btnimage = expan_btn.subsample(4,4)
percentage = Button(mainFrame, fg="black", image=expan_btnimage, bd=0, bg="black", cursor="hand2",
               command=lambda: expand()).grid(row=0, column=2, padx=1, pady=1)

divide = PhotoImage(file = r"images\divide.png")
divideimage = divide.subsample(4,4)
divide = Button(mainFrame, text="/", fg="white",image=divideimage, bd=0, bg="black", cursor="hand2",
                command=lambda: clickButton("/")).grid(row=0, column=3, padx=1, pady=1)


seven = PhotoImage(file = r"images\seven.png")
sevenimage = seven.subsample(4,4)
seven = Button(mainFrame, text="7", fg="black", image=sevenimage, bd=0, bg="black", cursor="hand2",
               command=lambda: clickButton(7)).grid(row=1, column=0, padx=1, pady=1)

eight = PhotoImage(file = r"images\eight.png")
eightimage = eight.subsample(4,4)
eight = Button(mainFrame, text="8", fg="black", image=eightimage, bd=0, bg="black", cursor="hand2",
               command=lambda: clickButton(8)).grid(row=1, column=1, padx=1, pady=1)

nine = PhotoImage(file = r"images\nine.png")
nineimage = nine.subsample(4,4)
nine = Button(mainFrame, text="9", fg="black", image=nineimage, bd=0, bg="black", cursor="hand2",
              command=lambda: clickButton(9)).grid(row=1, column=2, padx=1, pady=1)

multi = PhotoImage(file = r"images\multi.png")
multiimage = multi.subsample(4,4)
multiply = Button(mainFrame, text="*", fg="white",image=multiimage, bd=0, bg="black", cursor="hand2",
                  command=lambda: clickButton("*")).grid(row=1, column=3, padx=1, pady=1)

four = PhotoImage(file = r"images\four.png")
fourimage = four.subsample(4,4)
four = Button(mainFrame, text="4", fg="black", image=fourimage, bd=0, bg="black", cursor="hand2",
              command=lambda: clickButton(4)).grid(row=2, column=0, padx=1, pady=1)

five = PhotoImage(file = r"images\five.png")
fiveimage = five.subsample(4,4)
five = Button(mainFrame, text="5", fg="black", image=fiveimage, bd=0, bg="black", cursor="hand2",
              command=lambda: clickButton(5)).grid(row=2, column=1, padx=1, pady=1)

six = PhotoImage(file = r"images\six.png")
siximage = six.subsample(4,4)
six = Button(mainFrame, text="6", fg="black", image=siximage, bd=0, bg="black", cursor="hand2",
             command=lambda: clickButton(6)).grid(row=2, column=2, padx=1, pady=1)

minus = PhotoImage(file = r"images\minus.png")
minusimage = minus.subsample(4,4)
minus = Button(mainFrame, text="-", fg="white",image=minusimage, bd=0, bg="black", cursor="hand2",
               command=lambda: clickButton("-")).grid(row=2, column=3, padx=1, pady=1)

one = PhotoImage(file = r"images\one.png")
oneimage = one.subsample(4,4)
one = Button(mainFrame, text="1", fg="black", image=oneimage,bd=0, bg="black", cursor="hand2",
             command=lambda: clickButton(1)).grid(row=3, column=0, padx=1, pady=1)

two = PhotoImage(file = r"images\two.png")
twoimage = two.subsample(4,4)
two = Button(mainFrame, text="2", fg="black",image=twoimage, bd=0, bg="black", cursor="hand2",
             command=lambda: clickButton(2)).grid(row=3, column=1, padx=1, pady=1)

three = PhotoImage(file = r"images\three.png")
threeimage = three.subsample(4,4)
three = Button(mainFrame, text="3", fg="black",image=threeimage, bd=0, bg="black", cursor="hand2",
               command=lambda: clickButton(3)).grid(row=3, column=2, padx=1, pady=1)

plus = PhotoImage(file = r"images\plus.png")
plusimage = plus.subsample(4,4)
plus = Button(mainFrame, text="+", fg="white",image=plusimage, bd=0, bg="black", cursor="hand2",
              command=lambda: clickButton("+")).grid(row=3, column=3, padx=1, pady=1)


zero = PhotoImage(file = r"images\0.png")
zeroimage = zero.subsample(4,4)
zero = Button(mainFrame, text="0", fg="black",image=zeroimage, bd=0, bg="black", cursor="hand2",
              command=lambda: clickButton(0)).grid(row=4, column=0, columnspan=2, padx=1, pady=1)

point = PhotoImage(file = r"images\point.png")
pointimage = point.subsample(4,4)
point = Button(mainFrame, text=".", fg="black",image=pointimage, bd=0, bg="black", cursor="hand2",
               command=lambda: clickButton(".")).grid(row=4, column=2, padx=1, pady=1)


equal = PhotoImage(file = r"images\equal.png")
equalimage = equal.subsample(4,4)
equals = Button(mainFrame, text="=", image=equalimage, fg="white", bd=0, bg="black", cursor="hand2",
                command=lambda: equalButton()).grid(row=4, column=3, padx=1, pady=1)

bracket1 = PhotoImage(file = r"images\bracket1.png")
bracket1image = bracket1.subsample(4,4)
bracket1 = Button(mainFrame, text="pi", fg="black",image=bracket1image, bd=0, bg="black", cursor="hand2",
               command=lambda: clickButton("(")).grid(row=5, column=0, padx=1, pady=1)

bracket2 = PhotoImage(file = r"images\bracket2.png")
bracket2image = bracket2.subsample(4,4)
bracket2 = Button(mainFrame, text="pi", fg="black",image=bracket2image, bd=0, bg="black", cursor="hand2",
               command=lambda: clickButton(")")).grid(row=5, column=1, padx=1, pady=1)

pie=3.14159265358979323846264338327950288419716939937510
58209749445923078164062862089986280348253421170679
82148086513282306647093844609550582231725359408128
48111745028410270193852110555964462294895493038196
44288109756659334461284756482337867831652712019091
45648566923460348610454326648213393607260249141273
72458700660631558817488152092096282925409171536436
78925903600113305305488204665213841469519415116094
33057270365759591953092186117381932611793105118548
07446237996274956735188575272489122793818301194912
98336733624406566430860213949463952247371907021798
60943702770539217176293176752384674818467669405132
00056812714526356082778577134275778960917363717872
14684409012249534301465495853710507922796892589235
42019956112129021960864034418159813629774771309960
51870721134999999837297804995105973173281609631859
50244594553469083026425223082533446850352619311881
71010003137838752886587533208381420617177669147303
59825349042875546873115956286388235378759375195778
18577805321712268066130019278766111959092164201989
38095257201065485863278865936153381827968230301952
03530185296899577362259941389124972177528347913151
55748572424541506959508295331168617278558890750983
81754637464939319255060400927701671139009848824012
85836160356370766010471018194295559619894676783744
94482553797747268471040475346462080466842590694912
93313677028989152104752162056966024058038150193511
25338243003558764024749647326391419927260426992279
67823547816360093417216412199245863150302861829745
55706749838505494588586926995690927210797509302955
32116534498720275596023648066549911988183479775356
63698074265425278625518184175746728909777727938000
81647060016145249192173217214772350141441973568548
16136115735255213347574184946843852332390739414333
45477624168625189835694855620992192221842725502542
56887671790494601653466804988627232791786085784383
82796797668145410095388378636095068006422512520511
73929848960841284886269456042419652850222106611863
06744278622039194945047123713786960956364371917287
46776465757396241389086583264599581339047802759009
94657640789512694683983525957098258226205224894077
26719478268482601476990902640136394437455305068203
49625245174939965143142980919065925093722169646151
57098583874105978859597729754989301617539284681382
68683868942774155991855925245953959431049972524680
84598727364469584865383673622262609912460805124388
43904512441365497627807977156914359977001296160894
41694868555848406353422072225828488648158456028506
01684273945226746767889525213852254995466672782398
64565961163548862305774564980355936345681743241125
15076069479451096596094025228879710893145669136867
22874894056010150330861792868092087476091782493858
90097149096759852613655497818931297848216829989487
22658804857564014270477555132379641451523746234364
54285844479526586782105114135473573952311342716610
21359695362314429524849371871101457654035902799344
03742007310578539062198387447808478489683321445713
86875194350643021845319104848100537061468067491927
81911979399520614196634287544406437451237181921799
98391015919561814675142691239748940907186494231961
56794520809514655022523160388193014209376213785595
66389377870830390697920773467221825625996615014215
03068038447734549202605414665925201497442850732518
66600213243408819071048633173464965145390579626856
10055081066587969981635747363840525714591028970641
40110971206280439039759515677157700420337869936007
23055876317635942187312514712053292819182618612586
73215791984148488291644706095752706957220917567116
72291098169091528017350671274858322287183520935396
57251210835791513698820914442100675103346711031412
67111369908658516398315019701651511685171437657618
35155650884909989859982387345528331635507647918535
89322618548963213293308985706420467525907091548141
65498594616371802709819943099244889575712828905923
23326097299712084433573265489382391193259746366730
58360414281388303203824903758985243744170291327656
18093773444030707469211201913020330380197621101100
44929321516084244485963766983895228684783123552658
21314495768572624334418930396864262434107732269780
28073189154411010446823252716201052652272111660396
66557309254711055785376346682065310989652691862056
47693125705863566201855810072936065987648611791045
33488503461136576867532494416680396265797877185560
84552965412665408530614344431858676975145661406800
70023787765913440171274947042056223053899456131407
11270004078547332699390814546646458807972708266830
63432858785698305235808933065757406795457163775254
20211495576158140025012622859413021647155097925923
09907965473761255176567513575178296664547791745011
29961489030463994713296210734043751895735961458901
93897131117904297828564750320319869151402870808599
04801094121472213179476477726224142548545403321571
85306142288137585043063321751829798662237172159160
77166925474873898665494945011465406284336639379003
97692656721463853067360965712091807638327166416274
88880078692560290228472104031721186082041900042296
61711963779213375751149595015660496318629472654736
42523081770367515906735023507283540567040386743513
62222477158915049530984448933309634087807693259939
78054193414473774418426312986080998886874132604721
56951623965864573021631598193195167353812974167729
47867242292465436680098067692823828068996400482435
40370141631496589794092432378969070697794223625082
21688957383798623001593776471651228935786015881617
55782973523344604281512627203734314653197777416031
99066554187639792933441952154134189948544473456738
31624993419131814809277771038638773431772075456545
32207770921201905166096280490926360197598828161332
31666365286193266863360627356763035447762803504507
77235547105859548702790814356240145171806246436267
94561275318134078330336254232783944975382437205835
31147711992606381334677687969597030983391307710987
04085913374641442822772634659470474587847787201927
71528073176790770715721344473060570073349243693113
83504931631284042512192565179806941135280131470130
47816437885185290928545201165839341965621349143415
95625865865570552690496520985803385072242648293972
85847831630577775606888764462482468579260395352773
48030480290058760758251047470916439613626760449256
27420420832085661190625454337213153595845068772460
29016187667952406163425225771954291629919306455377
99140373404328752628889639958794757291746426357455
25407909145135711136941091193932519107602082520261
87985318877058429725916778131496990090192116971737
27847684726860849003377024242916513005005168323364
35038951702989392233451722013812806965011784408745
19601212285993716231301711444846409038906449544400
61986907548516026327505298349187407866808818338510
22833450850486082503930213321971551843063545500766
82829493041377655279397517546139539846833936383047
46119966538581538420568533862186725233402830871123
28278921250771262946322956398989893582116745627010
21835646220134967151881909730381198004973407239610
36854066431939509790190699639552453005450580685501
95673022921913933918568034490398205955100226353536
19204199474553859381023439554495977837790237421617
27111723643435439478221818528624085140066604433258
88569867054315470696574745855033232334210730154594
05165537906866273337995851156257843229882737231989
87571415957811196358330059408730681216028764962867
44604774649159950549737425626901049037781986835938
14657412680492564879855614537234786733039046883834
36346553794986419270563872931748723320837601123029
91136793862708943879936201629515413371424892830722
01269014754668476535761647737946752004907571555278
19653621323926406160136358155907422020203187277605
27721900556148425551879253034351398442532234157623
36106425063904975008656271095359194658975141310348
22769306247435363256916078154781811528436679570611
08615331504452127473924544945423682886061340841486
37767009612071512491404302725386076482363414334623
51897576645216413767969031495019108575984423919862
91642193994907236234646844117394032659184044378051
33389452574239950829659122850855582157250310712570
12668302402929525220118726767562204154205161841634
84756516999811614101002996078386909291603028840026
91041407928862150784245167090870006992821206604183
71806535567252532567532861291042487761825829765157
95984703562226293486003415872298053498965022629174
87882027342092222453398562647669149055628425039127
57710284027998066365825488926488025456610172967026
64076559042909945681506526530537182941270336931378
51786090407086671149655834343476933857817113864558
73678123014587687126603489139095620099393610310291
61615288138437909904231747336394804575931493140529
76347574811935670911013775172100803155902485309066
92037671922033229094334676851422144773793937517034
43661991040337511173547191855046449026365512816228
82446257591633303910722538374218214088350865739177
15096828874782656995995744906617583441375223970968
34080053559849175417381883999446974867626551658276
58483588453142775687900290951702835297163445621296
40435231176006651012412006597558512761785838292041
97484423608007193045761893234922927965019875187212
72675079812554709589045563579212210333466974992356
30254947802490114195212382815309114079073860251522
74299581807247162591668545133312394804947079119153
26734302824418604142636395480004480026704962482017
92896476697583183271314251702969234889627668440323
26092752496035799646925650493681836090032380929345
95889706953653494060340216654437558900456328822505
45255640564482465151875471196218443965825337543885
69094113031509526179378002974120766514793942590298
96959469955657612186561967337862362561252163208628
69222103274889218654364802296780705765615144632046
92790682120738837781423356282360896320806822246801
22482611771858963814091839036736722208883215137556
00372798394004152970028783076670944474560134556417
25437090697939612257142989467154357846878861444581
23145935719849225284716050492212424701412147805734
55105008019086996033027634787081081754501193071412
23390866393833952942578690507643100638351983438934
15961318543475464955697810382930971646514384070070
73604112373599843452251610507027056235266012764848
30840761183013052793205427462865403603674532865105
70658748822569815793678976697422057505968344086973
50201410206723585020072452256326513410559240190274
21624843914035998953539459094407046912091409387001
26456001623742880210927645793106579229552498872758
46101264836999892256959688159205600101655256375679
pi = PhotoImage(file = r"images\pi.png")
piimage = pi.subsample(4,4)
pi = Button(mainFrame, text="pi", fg="black",image=piimage, bd=0, bg="black", cursor="hand2",
               command=lambda: clickButton(pie)).grid(row=5, column=2, padx=1, pady=1)

eie = 2.7182
ee = PhotoImage(file = r"images\eie.png")
eeimage = ee.subsample(4,4)
ee = Button(mainFrame, text="pi", fg="black",image=eeimage, bd=0, bg="black", cursor="hand2",
               command=lambda: clickButton(eie)).grid(row=5, column=3, padx=1, pady=1)

sin_btn = PhotoImage(file = r"images\sin_btn.png")
sin_btnimage = sin_btn.subsample(4,4)
sin_btn = Button(mainFrame, text="sin", fg="black",image=sin_btnimage, bd=0, bg="black", cursor="hand2",
               command=lambda: clickButton("sin(")).grid(row=6, column=0, padx=1, pady=1)

cos_btn = PhotoImage(file = r"images\cos_btn.png")
cos_btnimage = cos_btn.subsample(4,4)
cos_btn = Button(mainFrame, text="cos", fg="black",image=cos_btnimage, bd=0, bg="black", cursor="hand2",
               command=lambda: clickButton("cos(")).grid(row=6, column=1, padx=1, pady=1)

tan_btn = PhotoImage(file = r"images\tan_btn.png")
tan_btnimage = tan_btn.subsample(4,4)
tan_btn = Button(mainFrame, text="tan", fg="black",image=tan_btnimage, bd=0, bg="black", cursor="hand2",
               command=lambda: clickButton("tan(")).grid(row=6, column=2, padx=1, pady=1)

log_btn = PhotoImage(file = r"images\log_btn.png")
log_btnimage = log_btn.subsample(4,4)
log_btn = Button(mainFrame, text="log", fg="black",image=log_btnimage, bd=0, bg="black", cursor="hand2",
               command=lambda: clickButton("log(")).grid(row=6, column=3, padx=1, pady=1)

expan = PhotoImage(file = r"images\expand.png")
expanimage = expan.subsample(4,4)
expan = Label(window, text="pi", fg="black",image=expanimage, bg="black").pack(side=BOTTOM)

window.iconbitmap("images\icon.ico")
window.config(bg="black",menu=menubar)
window.mainloop()
