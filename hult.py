import smtplib  #This library is used to open gmail server n work with it
import base64  #Encoding of content is done using this library
from email.mime.text import MIMEText   #To work with text portion of mail 
from email.mime.multipart import MIMEMultipart  # To attach imagaes or pdf or anything else
from email.mime.base import MIMEBase  
from email import encoders  # To encode

email_user = 'e-mail@address.com' # The Id from which mail will be sent
email_password = 'password'  #password of ID from which mail will be sent (It is only with u in ur IDE so safe to use totally)
while True:
    try:       
        email_send = input(str("Enter sender address"))  #Ask for entering E-mail address to whom mail to be sent
        
        paragraph=input("Enter paragraph")  #Ask for paragarph which has to be added in the middle of mail format.
                                            #It can be copied and pasted from google docs or anything
        #Subject of mail
        subject = 'Invitation to collaborate with the pioneer "Nobel Prize for Students - HultPrize@IOE: $1M challenge" 2020-21'

        msg = MIMEMultipart()
        msg['From'] = email_user  #Takes email address of ur ID
        msg['To'] = email_send  # Take email address of whom it wll be sent
        msg['Subject'] = subject  #Takes Subject

        #Make a format of email in google Doc which can be text with bold words and some words with link in it 
        #and download it as html not pdf or any other file type which is maileformat_html.html in this folder
        #We will be sending html mail not text coz if text is sent no bold wrods or attached links woth words will be seen
        #After being sent the receiver's browser will convert that html to beautiful text as we do while making website
        #Here "Love is not life" is the sentence which will be reeplaced by our sentence or paragraph
        #mailformat_html.html conatins html code of google sheet or simply mail format 
        #Open it with Notepad and type ctr + f search for "Love is not life" and copy all html code before that sentence and paste it
        #in first string variable and copy another portion of html code after sentence"Love is not life" and paste it in second string variable
        
        # we will concatenate first,second and paragraph as they are still string and assign it to one variable text


        first='''<html><head><meta content="text/html; charset=UTF-8" http-equiv="content-type"><style type="text/css">ol{margin:0;padding:0}table td,table th{padding:0}.c43{border-right-style:solid;padding:5pt 5pt 5pt 5pt;border-bottom-color:#3c3c3b;border-top-width:0pt;border-right-width:0pt;border-left-color:#3c3c3b;vertical-align:top;border-right-color:#3c3c3b;border-left-width:0pt;border-top-style:solid;border-left-style:solid;border-bottom-width:0pt;width:270pt;border-top-color:#808080;border-bottom-style:solid}.c23{border-right-style:solid;padding:1pt 1pt 1pt 1pt;border-bottom-color:#000000;border-top-width:0pt;border-right-width:0pt;border-left-color:#000000;vertical-align:top;border-right-color:#000000;border-left-width:0pt;border-top-style:solid;border-left-style:solid;border-bottom-width:0pt;width:174pt;border-top-color:#000000;border-bottom-style:solid}.c45{border-right-style:solid;padding:0pt 0pt 2pt 0pt;border-bottom-color:#444444;border-top-width:1pt;border-right-width:0pt;border-left-color:#444444;vertical-align:top;border-right-color:#444444;border-left-width:0pt;border-top-style:dotted;border-left-style:solid;border-bottom-width:0pt;width:360pt;border-top-color:#0b0a0b;border-bottom-style:solid}.c30{border-right-style:solid;padding:5pt 5pt 5pt 5pt;border-bottom-color:#0b0a0b;border-top-width:0pt;border-right-width:0pt;border-left-color:#444444;vertical-align:top;border-right-color:#444444;border-left-width:0pt;border-top-style:solid;border-left-style:solid;border-bottom-width:1pt;width:270pt;border-top-color:#131313;border-bottom-style:dotted}.c18{border-right-style:solid;padding:1pt 1pt 1pt 1pt;border-bottom-color:#000000;border-top-width:0pt;border-right-width:0pt;border-left-color:#0b0a0b;vertical-align:top;border-right-color:#0b0a0b;border-left-width:0pt;border-top-style:solid;border-left-style:solid;border-bottom-width:0pt;width:174pt;border-top-color:#000000;border-bottom-style:solid}.c7{border-right-style:solid;padding:2pt 0pt 0pt 1pt;border-bottom-color:#000000;border-top-width:0pt;border-right-width:0pt;border-left-color:#000000;vertical-align:top;border-right-color:#000000;border-left-width:0pt;border-top-style:solid;border-left-style:solid;border-bottom-width:0pt;width:174pt;border-top-color:#000000;border-bottom-style:solid}.c21{border-right-style:solid;padding:0pt 0pt 4pt 0pt;border-bottom-color:#0b0a0b;border-top-width:0pt;border-right-width:0pt;border-left-color:#1793d2;vertical-align:top;border-right-color:#1793d2;border-left-width:0pt;border-top-style:solid;border-left-style:solid;border-bottom-width:1pt;width:360pt;border-top-color:#3c3c3b;border-bottom-style:dotted}.c28{border-right-style:solid;padding:2pt 0pt 0pt 0pt;border-bottom-color:#0b0a0b;border-top-width:0pt;border-right-width:0pt;border-left-color:#444444;vertical-align:top;border-right-color:#444444;border-left-width:0pt;border-top-style:solid;border-left-style:solid;border-bottom-width:1pt;width:360pt;border-top-color:#444444;border-bottom-style:dotted}.c16{border-right-style:solid;padding:5pt 5pt 5pt 5pt;border-bottom-color:#1793d2;border-top-width:0pt;border-right-width:0pt;border-left-color:#1793d2;vertical-align:top;border-right-color:#1793d2;border-left-width:0pt;border-top-style:solid;border-left-style:solid;border-bottom-width:0pt;width:270pt;border-top-color:#3c3c3b;border-bottom-style:solid}.c51{border-right-style:solid;padding:0pt 0pt 4pt 0pt;border-bottom-color:#3c3c3b;border-top-width:0pt;border-right-width:0pt;border-left-color:#3c3c3b;vertical-align:top;border-right-color:#3c3c3b;border-left-width:0pt;border-top-style:solid;border-left-style:solid;border-bottom-width:0pt;width:360pt;border-top-color:#3c3c3b;border-bottom-style:solid}.c34{border-right-style:solid;padding:5pt 5pt 5pt 5pt;border-bottom-color:#131313;border-top-width:0pt;border-right-width:0pt;border-left-color:#444444;vertical-align:top;border-right-color:#444444;border-left-width:0pt;border-top-style:solid;border-left-style:solid;border-bottom-width:0pt;width:270pt;border-top-color:#1793d2;border-bottom-style:solid}.c35{border-right-style:solid;border-bottom-color:#131313;border-top-width:0pt;border-right-width:0pt;border-left-color:#131313;vertical-align:middle;border-right-color:#131313;border-left-width:0pt;border-top-style:solid;border-left-style:solid;border-bottom-width:0pt;width:270pt;border-top-color:#131313;border-bottom-style:solid}.c1{border-right-style:solid;border-bottom-color:#000000;border-top-width:0pt;border-right-width:0pt;border-left-color:#131313;vertical-align:middle;border-right-color:#131313;border-left-width:0pt;border-top-style:solid;border-left-style:solid;border-bottom-width:0pt;width:174pt;border-top-color:#131313;border-bottom-style:solid}.c32{border-right-style:solid;border-bottom-color:#444444;border-top-width:0pt;border-right-width:0pt;border-left-color:#444444;vertical-align:middle;border-right-color:#131313;border-left-width:0pt;border-top-style:solid;border-left-style:solid;border-bottom-width:0pt;width:90pt;border-top-color:#444444;border-bottom-style:solid}.c12{background-color:#ffffff;-webkit-text-decoration-skip:none;font-weight:400;text-decoration:underline;vertical-align:baseline;text-decoration-skip-ink:none;font-size:11pt;font-family:"Arial";font-style:normal}.c26{background-color:#ffffff;color:#888888;font-weight:400;text-decoration:none;vertical-align:baseline;font-size:11pt;font-family:"Arial";font-style:normal}.c39{background-color:#ffffff;color:#131313;font-weight:400;text-decoration:none;vertical-align:baseline;font-size:11pt;font-family:"Arial";font-style:normal}.c27{background-color:#ffffff;color:#0b0a0b;font-weight:400;text-decoration:none;vertical-align:baseline;font-size:11pt;font-family:"Arial";font-style:normal}.c10{background-color:#ffffff;color:#1155cc;font-weight:400;text-decoration:none;vertical-align:baseline;font-size:10pt;font-family:"Arial";font-style:normal}.c4{background-color:#ffffff;color:#e6007f;font-weight:400;text-decoration:none;vertical-align:baseline;font-size:34pt;font-family:"Arial";font-style:normal}.c9{background-color:#ffffff;color:#444444;font-weight:400;text-decoration:none;vertical-align:baseline;font-size:11pt;font-family:"Arial";font-style:normal}.c3{background-color:#ffffff;padding-top:0pt;padding-bottom:0pt;line-height:1.38;orphans:2;widows:2;text-align:justify}.c6{color:#000000;font-weight:400;text-decoration:none;vertical-align:baseline;font-size:11pt;font-family:"Arial";font-style:normal}.c25{color:#222222;font-weight:400;text-decoration:none;vertical-align:baseline;font-size:11pt;font-family:"Arial";font-style:normal}.c14{padding-top:0pt;padding-bottom:0pt;line-height:1.15;orphans:2;widows:2;text-align:left;height:11pt}.c15{padding-top:0pt;padding-bottom:0pt;line-height:0.9545454545454546;orphans:2;widows:2;text-align:left;height:11pt}.c17{padding-top:0pt;padding-bottom:0pt;line-height:1.15;orphans:2;widows:2;text-align:left}.c19{padding-top:0pt;padding-bottom:0pt;line-height:0.9545454545454546;orphans:2;widows:2;text-align:left}.c53{color:#000000;text-decoration:none;vertical-align:baseline;font-size:11pt;font-family:"Arial"}.c50{border-spacing:0;border-collapse:collapse;margin-right:auto}.c5{text-decoration-skip-ink:none;-webkit-text-decoration-skip:none;font-style:italic;text-decoration:underline}.c20{text-decoration-skip-ink:none;-webkit-text-decoration-skip:none;text-decoration:underline}.c37{background-color:#ffffff;color:#e6007f}.c38{background-color:#ffffff;color:#0b0a0b}.c46{font-size:24pt;color:#444444}.c24{color:inherit;text-decoration:inherit}.c47{max-width:778.5pt;padding:4.5pt 9pt 72pt 4.5pt}.c48{color:#ff00ff}.c2{font-weight:700}.c29{height:12pt}.c0{height:75pt}.c41{height:12.8pt}.c40{background-color:#ffffff}.c13{height:13.5pt}.c42{height:15pt}.c36{height:18.8pt}.c33{height:0pt}.c52{color:#131313}.c31{font-style:italic}.c22{height:11pt}.c49{color:#444444}.c8{height:11.2pt}.c44{height:28.5pt}.c11{color:#1155cc}.title{padding-top:0pt;color:#000000;font-size:26pt;padding-bottom:3pt;font-family:"Arial";line-height:1.15;page-break-after:avoid;orphans:2;widows:2;text-align:left}.subtitle{padding-top:0pt;color:#666666;font-size:15pt;padding-bottom:16pt;font-family:"Arial";line-height:1.15;page-break-after:avoid;orphans:2;widows:2;text-align:left}li{color:#000000;font-size:11pt;font-family:"Arial"}p{margin:0;color:#000000;font-size:11pt;font-family:"Arial"}h1{padding-top:20pt;color:#000000;font-size:20pt;padding-bottom:6pt;font-family:"Arial";line-height:1.15;page-break-after:avoid;orphans:2;widows:2;text-align:left}h2{padding-top:18pt;color:#000000;font-size:16pt;padding-bottom:6pt;font-family:"Arial";line-height:1.15;page-break-after:avoid;orphans:2;widows:2;text-align:left}h3{padding-top:16pt;color:#434343;font-size:14pt;padding-bottom:4pt;font-family:"Arial";line-height:1.15;page-break-after:avoid;orphans:2;widows:2;text-align:left}h4{padding-top:14pt;color:#666666;font-size:12pt;padding-bottom:4pt;font-family:"Arial";line-height:1.15;page-break-after:avoid;orphans:2;widows:2;text-align:left}h5{padding-top:12pt;color:#666666;font-size:11pt;padding-bottom:4pt;font-family:"Arial";line-height:1.15;page-break-after:avoid;orphans:2;widows:2;text-align:left}h6{padding-top:12pt;color:#666666;font-size:11pt;padding-bottom:4pt;font-family:"Arial";line-height:1.15;page-break-after:avoid;font-style:italic;orphans:2;widows:2;text-align:left}</style></head><body><div class="c40 c47"><p class="c3"><span class="c6">Dear sir/madam,</span></p><p class="c3"><span class="c6">&nbsp;</span></p><p class="c3"><span class="c6">Greetings from Hult Prize@IoE, Nepal !!!</span></p><p class="c3"><span class="c6">&nbsp;</span></p><p class="c3"><span>Hult Prize, also known as the</span><span class="c2 c31">&nbsp;Nobel Prize for students </span><span>and affiliated with the </span><span class="c2">United Nations</span><span>&nbsp;to achieve the sustainable development goals, is the biggest annual, year-long entrepreneurship competition organized </span><span class="c2">worldwide that crowd-sources idea</span><span class="c6">&nbsp;from university-level students after challenging them to solve a pressing social issue around many topics.</span></p><p class="c3"><span class="c6">&nbsp;</span></p><p class="c3"><span>I am Tunisha Gyawali from</span><span><a class="c24" href="https://www.google.com/url?q=http://www.nxtgennepal.org/&amp;sa=D&amp;ust=1604303452892000&amp;usg=AOvVaw2DLNpLYpbKpRj3wT-mHtgn">&nbsp;</a></span><span class="c2 c11"><a class="c24" href="https://www.google.com/url?q=http://www.nxtgennepal.org/&amp;sa=D&amp;ust=1604303452893000&amp;usg=AOvVaw0cunk5OCa5TeCM5DQW5K-X">NxtGen</a></span><span class="c2">&nbsp;</span><span>situated at the biggest engineering institute of Nepal, Institute of Engineering (</span><span class="c2">IoE</span><span>), Lalitpur, Nepal. </span><span class="c2">NxtGen</span><span>&nbsp;is a non-governmental and non-profit organization that has been organizing a number of national and international events focusing on personal development in youths and promoting social activities. Quantum Hack Hackathon, now titled the </span><span class="c2 c31">&quot;Largest digital hackathon of South Asia&quot; </span><span>was the last one of those conducted online with </span><span class="c2">2500+</span><span>&nbsp;audiences from </span><span class="c2">20+ countries</span><span>, in which our chief guest was </span><span class="c2">Steve Wozniak </span><span>(</span><span class="c2">co-founder of Apple</span><span class="c6">) and guests from Microsoft, Google, Facebook, and even celebrities.</span></p><p class="c3"><span class="c6">&nbsp;</span></p><p class="c3"><span class="c20 c2 c11"><a class="c24" href="https://www.google.com/url?q=http://www.hultprizeat.com/pulchowk&amp;sa=D&amp;ust=1604303452894000&amp;usg=AOvVaw2ZaJwesreRyehis9YEUk9d">Hult@IoE</a></span><span>&nbsp;is the </span><span class="c2">pioneer</span><span>&nbsp;of this franchise in Nepal and has had a successful reputation as a leading entity in the past years. &nbsp;This year, we are organizing this biggest online event with </span><span class="c2">12 colleges </span><span>and </span><span class="c2">1000+ participants</span><span>&nbsp;for bringing the best visionary ideas from students across the nation for competing for the</span><span class="c2">&nbsp;theme: </span><span class="c2 c31 c53">Food For Good.</span></p><p class="c3"><span class="c6">&nbsp;</span></p><p class="c3"><span>As a part of this grand event Hult Prize 2020-21, scheduled on </span><span class="c2 c20">November 28, 2020, </span><span>we have been conducting several pre-events each week, among which we have completed 4 out of </span><span class="c2 c5">8-leveled Entrepreneurship Talk Series</span><span>&nbsp;with speakers and guests like </span><span class="c2">Ali Zafar </span><span>(Bollywood star), </span><span class="c2">Preity Upala </span><span>(Hollywood entrepreneur and Miss India), </span><span class="c2">Satish Gaire,</span><span>&nbsp;</span><span class="c2">Pratik Gauri, </span><span>and</span><span class="c2">&nbsp;Scott Noppe-Brandon, </span><span>and also hosted </span><span class="c2">13 national and international celebrities</span><span>&nbsp;in our </span><span class="c2">&quot;Bada Dashain-Bada Event&quot;</span><span>&nbsp;session that have gained wide </span><span class="c2">media coverage </span><span class="c6">due to their grand success.</span></p><p class="c3 c22"><span class="c6"></span></p><p class="c3 c22"><span class="c6"></span></p><p class="c3"><span class="c6">'''
        second='''</span></p><p class="c3 c22"><span class="c6"></span></p><p class="c14 c40"><span class="c25"></span></p><p class="c3"><span class="c6">Attached herewith is the proposal for our event in detail. If you have any queries, please mail us at this same email. We are open to customize the scheme for the partnership to accommodate that of your interest. We&#39;d love to hear from you to discuss this further. </span></p><p class="c3"><span class="c6">&nbsp;</span></p><p class="c3"><span class="c6">Hoping for a positive response.</span></p><p class="c3"><span class="c6">&nbsp;</span></p><p class="c3"><span class="c6">Thank You.</span></p><p class="c3"><span class="c6">&nbsp;</span></p><p class="c3"><span class="c6">Kind regards, </span></p><p class="c14 c40"><span class="c6"></span></p><p class="c17"><span class="c26">--</span></p><a id="t.be55d4c69439412624afaff3245c96b52ca7389e"></a><a id="t.0"></a><table class="c50"><tbody><tr class="c13"><td class="c51" colspan="2" rowspan="1"><p class="c19"><span class="c37 c2">Tunisha Gyawali</span></p></td></tr><tr class="c13"><td class="c21" colspan="2" rowspan="1"><p class="c19"><span class="c37">Sponsors Coordinator</span></p></td></tr><tr class="c29"><td class="c45" colspan="2" rowspan="1"><p class="c19"><span class="c9">&nbsp;</span></p></td></tr><tr class="c0"><td class="c32" colspan="1" rowspan="1"><p class="c19"><span class="c40 c46">&nbsp;</span><span class="c4">Hult</span></p><p class="c19"><span class="c4">Prize</span></p></td><td class="c35" colspan="1" rowspan="1"><p class="c14"><span class="c39"></span></p><a id="t.2e4bc22a4ad5cfcdeb6b60764fb8499dee7fd73a"></a><a id="t.1"></a><table class="c50"><tbody><tr class="c33"><td class="c1" colspan="1" rowspan="1"><p class="c14"><span class="c39"></span></p></td></tr><tr class="c42"><td class="c23" colspan="1" rowspan="1"><p class="c17"><span class="c38">+977 9849272032</span></p></td></tr><tr class="c41"><td class="c18" colspan="1" rowspan="1"><p class="c17"><span class="c10">074bce185.tunisha@pcampus.edu.np</span></p></td></tr><tr class="c44"><td class="c23" colspan="1" rowspan="1"><p class="c17"><span class="c27">Pulchowk, Lalitpur, Nepal</span></p><p class="c17"><span class="c40 c52">&nbsp;</span><span class="c20 c40 c11"><a class="c24" href="https://www.google.com/url?q=http://www.hultprizeat.com/pulchowk&amp;sa=D&amp;ust=1604303452972000&amp;usg=AOvVaw0W02qw9ZpwtZ9lWL0nFkDe">www.hultprizeat.com/pulchowk</a></span></p></td></tr><tr class="c36"><td class="c7" colspan="1" rowspan="1"><p class="c14"><span class="c39"></span></p></td></tr></tbody></table><p class="c15"><span class="c9"></span></p></td></tr><tr class="c8"><td class="c28" colspan="2" rowspan="1"><p class="c19"><span class="c40 c49">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="c40 c48">&nbsp;</span></p></td></tr></tbody></table><p class="c14"><span class="c6"></span></p></div></body></html>'''
        text=first + paragraph + second  # concatenation of 3 parts of html of code
        body = str(text)  #Convertion of text string again to string and assigning it to body variable
        msg.attach(MIMEText(body,'html'))  #Attaching this string as html script with message

        filename='HP@IoE20-21_Proposal.pdf'  # Name of atttachment to be sent.Must be in same folder as code
        attachment  =open(filename,'rb')      # open attachment and read  it

        part = MIMEBase('application','octet-stream')  # As attachment is pdf "application" is used as content type
        part.set_payload((attachment).read())
        encoders.encode_base64(part)  #Encoded before being sent trough mail
        part.add_header('Content-Disposition',"attachment; filename= "+filename)  # This part is sent as attachment

        #2nd attachment
        filename_1='HP_SponsorshipPackage.pdf'
        attachment  =open(filename_1,'rb')

        part_1 = MIMEBase('application','octet-stream')
        part_1.set_payload((attachment).read())
        encoders.encode_base64(part_1)
        part_1.add_header('Content-Disposition',"attachment; filename= "+filename_1)

        
        msg.attach(part)  # Attachment is attached with main body of mail
        msg.attach(part_1) #same
        text = msg.as_string()  # Here the main thing happens where htl code is seen as clear formatted text in gmail inbox or   #simply  browser
        server = smtplib.SMTP('smtp.gmail.com',587)  #gmail server is selected and port number
        server.starttls()
        server.login(email_user,email_password)  # Login into your address is done
        server.sendmail(email_user,email_send,text)  # mail is sent
        server.quit()  # server is closed
        print("Mail successfully sent")
        continue
    except:
        print("Either email is wrong or soemthing else")  #Diplay msg is=f recipents id is wrong or something problems happens
        continue
    
        
    
