from query_optimise import SubQuery

# Initialize an empty list to store examples
examples = []

# Define the main question and corresponding sub-questions
questions = [
    ("What does “camping on a cell” mean?", "Define 'camping on a cell'."),
    ("What’s the frequency range on Band n77?", "Specify the frequency range for Band n77."),
    ("What’s an Inter-RAT Handover?", "Explain the concept of Inter-RAT Handover."),
    ("In what CR was the change for 'inter-RAT handover' introduces?", "Identify the CR introducing the change for 'inter-RAT handover'."),
    ("What’s the need-code for parameter 'YYY'?", "Provide the need-code for the parameter 'YYY'."),
    ("What’s the cell selection in the procedure?", "Describe the cell selection process."),
    ("How UE sync to cell?", "Explain how a UE synchronizes to a cell."),
    ("Could you tell more about PSS?", "Provide additional information about PSS."),
    ("How about PBCH?", "Share more details about PBCH."),
    ("Any more information about MIB and SIB?", "Provide additional details about MIB and SIB."),
    ("What’s DMRS? How it has been designed?", "Define DMRS and discuss its design."),
    ("What’s the difference between DMRS type 1 and type 2?", "Highlight the differences between DMRS type 1 and type 2."),
    ("What’s the difference between PDSCH and PDCCH?", "Differentiate between PDSCH and PDCCH."),
    ("How PDCCH is mapped to physical resource blocks?", "Explain the mapping of PDCCH to physical resource blocks."),
    ("Do you know anything for channel coding?", "Discuss channel coding."),
    ("How many different formats of PUCCH exist?", "Identify the different formats of PUCCH."),
    ("Please tell me how many slots on SCS 60kHz?", "Provide the number of slots for SCS 60kHz."),
    ("Please tell me how many PRB on 5G NR 100M?", "Provide the number of PRB for 5G NR with 100M."),
]

# Create a SubQuery object for each question pair and add it to the examples list
for question, sub_query in questions:
    example = SubQuery(question=question, sub_query=sub_query)
    examples.append(example)
###exampl#es.append({"input": question, "tool_calls"#: queri#es#})#
######
######
######
#1. #**W#hat does “camping on a cell” me#an?#**###
 #  - #W#hat is t#he #concept of "camp#ing on a cell" in telecommunicat#ion#s?###
# #  - How do#es ##a m#obi##le device# choose w#hich cell to camp on in a cellular net#work##?###
 ####  - What f#actors i#nflu#e#nce the decision for a mobile device to camp on ##a s#pecific# c#ell?#
###   - Can you expla#in the proc#ess of camping on a cell during network r#eg#istrat#io#n#?
#######
#2##. #**What’##s the frequency range on Band n#77#?#**###
 #  -# What# is t#he frequenc#y range cov#ered by Band n77 in cellular netw#or#k#s?###
  # - How does Band n#77 fi#t into# the o#verall sp#ectrum allocation for mobile# communica#tion##?###
 #####  - Are there any specific r#egulations or s#tandards related to the frequency range of #Band n##77?##
#####  ## - What are the implications of operating# within the frequency range of Band n77 fo#r network performa#nc#e#?
#########
#3. **W#hat’s an Inte#r-RAT Handov#er#?#*#*#####
 #  - What does #Int#er-RAT Hando#ver refer to in the context o#f mo#bile c##omm#unicat#ion?###
 #  -## How does# Inter-RA#T# Ha#ndover fa#cilitate seamless connectivi##ty be###tween differ#ent radio access technolog#ies?
 #### # -# Can you describe the ##process involv#ed in an Inter-RAT Handov##er?####
###   #- What are the challenges a#ssociated# with implementing Inter-RAT Handover in heterogeneous net#wo#rks##?###
#########
#4. *##*In what CR was the change for “inter-RAT handover” int#rodu#c#ed?*###*###
   ##- W#hat i#s a Change Reque#st (CR) in the context of 3GPP stand##ard#s?#####
  # #- Can y#ou identi#fy the s#peci#fic Change Request that intro#duced the## concept of Inter-RAT ##Hando####ve#r?
 ## # -## What were the obje#ctives# or motivati#ons behind proposing the change for Inter-RAT Hando#v##e#r?##
#### #  - How did the introducti#on of Inter-R#AT Handover impact existing network architectures a#nd #proto#c#ol##s##?
#########
#5.# *#*What’s the need-code for parameter “YY#Y”#?#*#*#######
 #  #-# W#hat role does parameter "YYY" play in #the configurati#on o##r ope####ration of cellular# networks?
 # # #-# #How is pa#rameter "YYY" #used in netw#ork proto#cols or proced#ures##?####
 ##  ##-# Can you explai#n the s#ignifica#nce of parameter "YYY" in optimizing network performance## or eff#icie#ncy?
#####  # - Are there any stan#dardizatio#n efforts or guidelines related to #the usage of paramete#r "Y#YY"#?
##########
#6.# #*#*What’s the cel#l selecti#on in the procedu#re?#*#*####
 #  -# Ho#w does cell selectio#n con#tribute to# the process of e#stab##lishi###ng n#etwork connectivity for mobile devices?
  # -## What criteria are c#on#sidered d#u##ri#ng the ce#ll selection pro#cess##?###
 ## # -# Can you describe #the algo#rithm or## mechanism used for ce#ll select#ion in cellular n#etw#or##ks#?#
####  # - What are the implication#s of cell sel#ection on network #handove##r# and resource allocat#i#on#?#
#########
#7#. *##*How does UE sync to ce#ll#?#**########
   #-# What steps does a Use#r Equipmen#t (U##E) device take to s#ynchronize with a cell in a cellular net##wor#k?####
 # # #- Can you explain the s#ynchroniz#ation# pro#cedure used by UE#s to establish timing and frequency alignme##nt wi###th the serving c##ell?
 ######  - What signaling messages are exchanged# between the# UE and the network during the synchronizati#on proce##ss?##
###### #  -# Are there any challenges or considerations assoc#iated with UE# synchronization in different #deployment sce#n#ar#ios#?##
###########
###8.# #*#*Could# you tell# more about P#SS?#**######
 ## # - What does PSS stan#d for #in the context of cellular netw###ork#s?####
 ###  - #Can you describe the pu#r#pose and #function of Primary Synch#ro##ni#zat###ion Signal (PSS) in LTE or 5G netwo##rks?
 ## # ##- How is the PSS signal genera#ted and transmitted by base s#tat#i#o##ns?####
###### #  - What role does the PSS play# in the initial cell search #and synchro##nization process for #UEs##?#
##########
##9#. *#*How about# PB#CH#?#**########
   #- #What is PBCH#, and what is its role in LTE or #5G n#etw#ork###s?####
 # ## - Can #y#ou# #explain t#he purpose and significance of t###he Ph###y#s#ical Broadcast Channel (PBCH) in the downlink transmiss###ion?
 ## # #- How is PB#C#H encoded and modulated before transmi#ssi##on?#####
#####  # - What informa#tion is typically conveyed through# the PBCH to## UEs during initial cell search and synch#ronizat#i#on#?
###########
##1#0.# **##An#y more information about MIB and S##IB?#**######
  #  - W#hat do M#IB and SIB stand for i#n the context of cellular n#etw##ork#s?####
 ##   -# ##Can you e#xpl#ain the purpose #and conte#nt of the M#aster# I#nf#ormation# Block (##MIB) ###and System Information Blocks (SI##Bs)?
 ## # # - Ho##w are MI#B and SI#Bs transmitted to UEs, and what #inf#ormation #do they c#ont#a#in?##
######  #  - Are t#here differe#nt types of SIBs, and how #are th#ey organized within #the netw#ork###?
############
##1#1###. ##*#*What#’s #DMRS? How it has been design#ed?#**######
  #  #- Wh#at #is ##DMRS, and what role does i#t play in# LTE or 5G com#munic#at#ion#s?###
 ##   - Ca#n yo#u #descr#ibe# th#e design pri#nciples a#nd structure of De#modul#ati##on #Re###ference Signal (DM##RS)?
 ###  # - How #are DMRS symbols #ge#nerated and mapped# in the time-frequen#cy doma##in?##
######## #   - What are the considerati#ons for DMRS des#ign to optimiz#e channel estimat#ion and demodulation performa#nce#?
##########
#1#2.# ##**What’s# the dif#ference between DMRS type 1 and #type# 2?#*#*####
 #   - Can yo#u exp#la#in the dist#inction between DMRS T#ype 1 and Type 2 configurat#ion#s?###
 ##   - What #are the d#i##fferences# i#n the generation# and mapp#ing of DMRS #symbo#ls for T#ype 1 and Ty##pe 2 ###configurati##ons?
 ### #  - Are there specifi##c use c#ases or #scenarios where one type of DMRS i#s prefer#red over the o#th#e#r?###
#### ##   - How do DMRS Type 1 a#nd Type 2 c#onfigurations impact cha#nnel estimation and# receiver complex##ity###?
#########
#1#3. ##*#*W#hat’s the dif#ference b#etween PDSCH and PDC#CH?#*#*####
 #   - What d#o PDSCH# and# PDC#CH stand for, and what are their respective functions in# LTE# o#r 5G## #downlink transmission?#
  # ## - Can you de#scribe #the #differe#nces in the information carried by PDSCH an#d PDCCH ch##a#n#nel#####s?#
 ## ##  - How are PDSCH and P#DCCH signals #mapped to physical re#sources #in the dow#nlink subf#ra##me?######
### #   - What are the implications of the differences between# PD#SCH #and PDCCH for system performance and# resource allocat#io##n###?
########
##14#.## **How PDCC#H is mapped to physical resource bloc#ks#?#*#*########
  #  #- Can ##y#ou explain the process of# mapping PDCC#H to physica#l re#so#urce# blo#cks (PRB#s) in LTE# or 5G downlink transmiss#ion?
# ### ##  -# W#ha#t# signaling and control i#nformation is# conveyed# through the PDCCH chan##nel?###
######    -# #How####
###########
 ##are# PDCCH #resources #allocated dynam##ically based# #on system requiremen#ts and UE feedba##ck?####
####   # - Are t#here specific resource alloca#tion sche#mes# or algori#thms u#sed for mapping PDCCH to PRBs in different deployment #scenar##ios#?
########
###15#. **D#o #you know anythi#ng for channel codi##ng?#**####
    #-# What #is #channel #c#oding, and why# i#s it essential in wireless communication sys#tem#s?###
 # #  - Can you desc#rib#e the pri#n#ciples## of #cha#nnel coding techniques such as convo#lutional# coding, Turb##o cod###ing, or LDPC cod#ing?
# ###   - How does channel coding impr##ove t#he reliabi#li#ty and robustness of communicati#on over no#isy channe##ls?####
#####  #  - Are there specific channel codi#ng standards or proto#cols adopted in LTE or 5#G systems, a#nd how do they differ in performance and com#plex##ity#?
#########
##16.# ##**#How many #di#fferent formats of PUCCH exi#st?##**###
   # - What is P#U#CCH#, and what role# does i#t play in LTE or 5G uplink transmis#sio#n?###
 #   #- Can you #identify #t##he differe#nt f##ormats o#r configurations of Physical Upli#nk Control Channel ##(PUCC####H)?
# ####   - How are PUCCH format##s selected# or# configu#red based# on system requirements# and channel conditio##ns?#####
### #   - Are there trade-offs be#tween different PUCCH form#ats in terms of signaling overhead, reliability, and e#ffi##cie##ncy#?
##########
#17.## #*#*Please# tell me ho#w many slots #on SCS 60k#Hz?##**###
 #   - What is Slo#t Con#figu#ration (#SCS), and how does it rel#ate to subcarrier spacing i#n LT#E or 5###G?#
 #   - Can you calcula#te t#h#e nu#mber of slots available within a given subframe with a subca##rrier### spacing of 60 #kHz?
 ### #  - How does the number of## slots per su#bf#rame im##pact sy#stem capacity and resource allocati##on?###
##### #   - Are there variations in slot configu#ration #based on different subcarrier spacings and deploy#ment sc#enar##ios#?
#######
#1##8. #**Please tell me# how m#any PRB on 5G NR 10#0M#?##**###
 #   - What is Physi#cal R#eso#urce Block (PRB), and how is it defined in 5G New Radio ##(NR#)?####
    #- Can you calculate the #number of PRBs availab#le within a bandwidth of 100 MHz in 5#G NR###?###
 ###  # - How does the number of PRBs affect the #data rate and throughput capabilities of a 5G NR sys#t#em?##
###    - Are there constraints or limitations on t#he allocation of PRBs based on regulatory re#quirements #or network configuration?
####
