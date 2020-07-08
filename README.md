# 2020-project-2-bitsplease

# Question 1
* Σύνδεση στο link που δίνεται από την εκφώνηση.
* Είδαμε ότι γίνεται directory listing (πχ /js)
* Εντοπισμός της σελίδας /server-info
* Εντοπισμός δυνατότητας αλλαγής visitor number μέσω του cookie 
  (αναγνώριση κωδικοποίησης base64 από το = στο τέλος και έπειτα αναζήτησης του hash και αναγνώριση του sha256)
* Εντοπισμός δεύτερου link ( jt4grrjwzyz3pjkylwfau5xnjaj23vxmhskqaeyfhrfylelw4hvxcuyd.onion ) μέσω του server-info
* Στο δεύτερο link, προσπαθώντας να συνδεθούμε, είδαμε στο link αναφορά στη σελίδα /access.php, της οποίας είδαμε 
  στη συνέχεια τον κώδικα (access.phps, όπως επιτρέπουν οι ρυθμίσεις του server-info: SetHandler application/x-httpd-php-source).
* Ακολουθώντας τις οδηγίες στα σχόλια του κώδικα, βρήκαμε το πολλαπλάσιο του 7 που ζητούνταν (1337) και προσθέσαμε 3 μη αριθμητικούς
  χαρακτήρες στο τέλος, ώστε να φτάσει το απαιτούμενο μέγεθος (1337aaa) των 7 χαρακτήρων.
* Για να καταφέρουμε να προσπεράσουμε και τον κωδικό, εκμεταλλευτήκαμε το bug της strcmp στην php, όπου επιστρέφει 0 (NULL),
  εαν το ένα όρισμα είναι λάθος τύπου. Βάλαμε λοιπόν url --> password[]=&user=1337aaa και περάσαμε τον έλεγχο.
* Αφού περάσαμε τον έλεγχο, είδαμε το μήνυμα και πήγαμε στη σελίδα /blogposts7589109238
* **Περιηγηθήκαμε στα posts της Υβόννης, βρήκαμε το github (https://github.com/chatziko/pico ), βρήκαμε το καινούργιο link (4tpgiulwmoz4sphv.onion) και την αναφορά στο Plan X.**
* Δοκιμάσαμε να βρούμε κι άλλα post της Υβόννης (πχ diary3.html), όμως δεν υπήρχαν. Κάνοντας όμως directory listing στο /blogposts7589109238/blogposts/
  βρήκαμε την καταχώρηση post3.html, όπου έλεγε μέσα ένα secret (racoon), το όνομα του Γιώργου(!!) και ένα visitor id.
* Βάζοντας το visitor id στο cookie με τον τρόπο που βρήκαμε πριν, οδηγηθήκαμε στη σελίδα 2fvhjskjet3n5syd6yfg5lhvwcs62bojmthr35ko5bllr3iqdb4ctdyd.onion/sekritbackups2444/
* Κατεβάσαμε τα αρχεία της σελίδας και προκειμένου να βρούμε το κλειδί, δοκιμάσαμε διάφορες ημερομηνίες που βρήκαμε στο site σε συνδυασμό με το secret racoon και αφού αποτύχαμε, 
  κάναμε brute force ημερομηνίες (for i in {1..400}; do echo -n $(date -I -d "2020-01-01 +$i days") raccoon | sha256sum >> dates.txt; done)
  και βρήκαμε ποια περιέχει το κρυπτογραφημένο truncated κομμάτι που είχε "ξεφύγει" από τη διαγραφή. Στη συνέχεια το χρησιμοποιήσαμε για αποκρυπτογράφηση.
* Στα αποκρυπτογραφημένα αρχεία βρήκαμε κρυμμένο ανάμεσα σε link για μια ταινία (θα τη δούμε μετά :P) το link προς ένα github repository (https://github.com/asn-d6/tor/) καθώς και το hash ενός commit (2355437c5f30fd2390a314b7d52fb3d24583ef97). 
* To commit που βρήκαμε είχε οδηγίες για να βρούμε το Γιώργο and we did it :)

# Question 2
Αφού τελειώσαμε με την πρώτη ερώτηση, το στοιχείο που δεν είχαμε ακολουθήσει ήταν αυτό που βρίσκεται παραπάνω σε bold, οπότε ξεκινήσαμε από εκεί.
* Χρησιμοποιήσαμε το username admin για να δούμε αν υπάρχει και υπήρχε! (Το καταλάβαμε γιατί έβγαλε invalid password, όχι invalid user, όπως πριν.
* Παρατηρήσαμε ότι η σύνταξη μιας printf προκαλούσε warning. Συνειδητοποιήσαμε ότι στη θέση του string που διευκρινίζει τι τύπου μεταβλητές θα εκτυπωθούν, βρισκόταν μια μεταβλητή. Δοκιμάσαμε λοιπόν, μαζί με το όνομα του χρήστη (admin) να βάλουμε εκτυπώσεις μεταβλητών (πχ %p), ώστε να εκτυπώσουμε τιμές μεταβλητών. Επειδή στην κλήση της printf δεν υπήρχαν μεταβλητές ενώ εμείς τις ζητούσαμε, καταφέραμε να εκτυπώσουμε τιμές θέσεων μνήμης που δεν θα έπρεπε να μπορούμε να δούμε. Μετά από δοκιμές, καταφέραμε να εκτυπώσουμε το hash του κωδικού του admin (%p %p %p %p %p %p %s --> f68762a532c15a8954be87b3d3fc3c31).
*  Αφού βρήκαμε το hash, χρησιμοποιήσαμε το https://crackstation.net/ για να καταλήξουμε στον κωδικό "you shall not pass" και μπήκαμε στην πρώτη σελίδα που έκρυβε ο σύνδεσμος. Εκεί βρήκαμε το στοιχείο που έλειπε από το Plan X, αλλά και αναφορά στο Plan Y.

# Question 3
Το μόνο μας στοιχείο σε αυτή τη φάση ήταν η φόρμα της σελίδας. Προφανώς δεν είχαμε τα στοιχεία που χρειάζονταν για να συνδεθούμε με κανονικό τρόπο, οπότε αρχίσαμε να ψάχνουμε πως θα μπορέσουμε να λύσουμε αυτό το πρόβλημα. Παρατηρώντας τον κώδικα του server είδαμε ότι:
* Υπάρχει ειδική κλήση που μας φέρνει την επόμενη σελίδα (serve ultimate).
* Μπορούμε να εκμεταλλευτούμε τη συνάρτηση post_param, στέλνοντας δικό μας αίτημα, το οποίο θα προκαλέσει buffer overflow.
Προσπαθώντας να πραγματοποιήσουμε την επίθεση στον τοπικό μας server, ήρθαμε αντιμέτωποι με τα canaries. Μετά από googlάρισμα (π.χ. https://access.redhat.com/blogs/766093/posts/3548631) και δοκιμές, βρήκαμε τη θέση του canary. Επειδή στη συγκεκριμένη περίπτωση η τιμή των canaries ήταν σταθερή σε όλα τα σημεία του προγράμματος, το να παρακάμψουμε αυτή την προστασία ήταν σχετικά εύκολο. Χρειάστηκε επίσης να βρούμε το offset του return address της check_auth (vulnerable σε buffer overlook, οπότε τη χρησιμοποιήσαμε για να βρούμε την πραγματική τιμή) από την εντολή κλήσης της serve_ultimate, που ήταν η συνάρτηση που μας ενδιέφερε (μέσω gdb). Το offset είναι σταθερό καθώς ο κώδικας αποθηκεύεται συνεχόμενα στη μνήμη και για αυτό προσπαθούμε να το εκμεταλλευτούμε. Υπάρχει ανεβασμένο python script (convert.py), το οποίο χρησιμοποιήθηκε ώστε να παράξουμε ένα κακόβουλο αρχείο, που στη συνέχεια στείλαμε μέσω postman στο server για να κάνουμε την επίθεση. Το script παράγει τα εξής:
* Αρκετοί χαρακτήρες ώστε να γεμίσει το vulnerable buffer.
* Η τιμή του canary που βρήκαμε, ώστε να μην blockαριστεί το αίτημά μας.
* Η διεύθυνση της εντολής κλήσης της serve_ultimate, η οποία παράγεται μέσω υπολογισμού (πρόσθεση του offset που βρήκαμε από gdb στο return address που βρήκαμε από την printf της check_auth).
Αφού δημιουργήσαμε το αρχείο και το στείλαμε μέσω postman, λάβαμε το στοιχείο που χρειαζόμασταν ώστε να ολοκληρώσουμε το βήμα 3.

Ο server μετά το αίτημά μας crashάρει, καθώς έχουμε παρέμβει στην ομαλή του λειτουργία (πχ δεν υπάρχει κάτι στο given_psw κάτι για να γίνει free). Αν ήμασταν καλοί hackers θα είχαμε φροντίσει να αφήσουμε τη μνήμη σε κατάσταση που δεν θα προκαλούσε πρόβλημα στη λειτουργία του server, ώστε να μην αφήσουμε ίχνος στα logs του συστήματος.

# Question 4
### Βήμα 4α
Η απάντηση του server στο προηγούμενό μας αίτημα ζητούσε να πάρουμε το log από το server. Η πρώτη μας σκέψη ήταν να χρησιμοποιήσουμε τη system από τη βιβλιοθήκη του συστήματος, αλλά με μια δεύτερη ματιά στον κώδικα είδαμε ότι μπορούμε να χρησιμοποιήσουμε τη send_file. Επιλέξαμε να χρησιμοποιήσουμε τη send_file γιατί ήταν πιο εύκολο. Η λογική που ακολουθήσαμε ήταν παρόμοια με αυτή του προηγούμενου ερωτήματος (buffer overflow στην post_param, υπολογισμοί offset για return address στο σωστό σημείο). Το διαφορετικό σε αυτό το ερώτημα ήταν το να μπορέσουμε να περάσουμε στη συνάρτηση το κατάλληλο όρισμα για να πετύχουμε αυτό που θέλουμε. Για να δεχτεί το όρισμα η συνάρτηση έπρεπε να της δώσουμε ένα pointer στο κατάλληλο string (όνομα του αρχείου που ψάχναμε). Το string ("/var/log/z.log\x00") δεν υπήρχε στο πρόγραμμα, οπότε έπρεπε να το συμπεριλάβουμε και αυτό στο κείμενο με το οποίο θα κάναμε buffer overflow. Για να βρούμε λοιπόν τη διεύθυνση μνήμης που το τοποθετήσαμε, έπρεπε να ξέρουμε κάποια διεύθυνση στη στοίβα. Αυτό και πάλι επιτεύχθηκε με buffer overlook και υπολογισμό offset, απλά αυτή τη φορά η διεύθυνση βάσης που χρησιμοποιήσαμε για τους υπολογισμούς μας αφορούσε τον ebp. Αφού καταφέραμε να δημιουργήσουμε το σωστό αίτημα, το στείλαμε στο server (python script hack.py και για τη δημιουργία και για την αποστολή) και πήραμε το στοιχείο για το επόμενο βήμα. Τα στοιχεία που χρειαστήκαμε για να συνδεθούμε στο server μέσω του script ήταν διαθέσιμα μέσω του link που βρήκαμε στα στοιχεία του ερωτήματος 3.

Πιο αναλυτικά για overlook και υπολογισμό offset για στοίβα:
* Παίρνουμε από τη στοίβα, μέσω buffer overlook στη check_auth, την τιμή του ebp της προηγούμενης συνάρτησης. Η τιμή αυτή αφορά την αρχή της συνάρτησης που καλεί την check_auth, άρα αφορά τη route.
* Εφόσον η route καλεί και την check_auth και την post_param, θα παραμείνει αμετάβλητη στη στοίβα, στη θέση την οποία έχουμε βρει.
* Η πρώτη μεταβλητή της post_param είναι ένας πίνακας post_data, του οποίου τη διεύθυνση μπορούμε να βρούμε.
* Βρίσκουμε τη διαφορά τους και έχουμε μια διεύθυνση βάσης για να βρούμε τη θέση του string και να την βάλουμε σαν όρισμα (pointer).

**Σχόλιο:** Στο script μας χρησιμοποιούμε ειδικό τρόπο επικοινωνίας και όχι postman, καθώς το postman δεν εμφανίζει το αποτέσμα της send_file αν δεν λάβει πρώτα κάποιο header.

### Βήμα 4β
Αφού λάβαμε το στοιχείο από το 4α, έπρεπε να βγάλουμε άκρη με δύο πράγματα. Το πρώτο ήταν το next-move και το δεύτερο το ip. Το next-move, μετά από googlαρισμα ανακαλύψαμε ότι αναφέρεται σε ένα παιχνίδι σκάκι (Deep Blue versus Kasparov, 1997, Game 6) και συγκεκριμένα η επόμενη κίνηση είναι και η νικητήρια! Για να πάρουμε το ip ενός μηχανήματος μπορούμε να χρησιμοποιήσουμε συγκεκριμένη εντολή στο terminal. Επειδή όμως δεν είμαστε στο δικό μας μηχάνημα, δεν μπορούμε να τρέξουμε την εντολή. Όμως μπορούμε να κάνουμε ret2libc και να βάλουμε τη system να το κάνει για εμάς. Αφού χρησιμοποιήσουμε τη system για να εμφανίσουμε την ip σε ένα αρχείο στο server, μπορούμε να χρησιμοποιήσουμε το script του προηγούμενου ερωτήματος (ζητώντας το /tmp/aabb.log αντί για το z.log) για να πάρουμε το αρχείο αυτό και να δούμε την ip. Έτσι φτάσαμε στο τέλος της εργασίας. Η κλήση της system μέσω ret2libc, γίνεται μέσω script (hack2.py), το οποίο λειτουργεί με τον εξής τρόπο:
* Το κομμάτι του overflow είναι παρόμοιο με πριν.
* Σε αυτή την περίπτωση δεν χρειαζόμαστε κάποια συνάρτηση η οποία βρίσκεται στον κώδικά μας, αλλά μια συνάρτηση η οποία βρίσκεται στη stdlib, οπότε πρέπει να ψάξουμε σε πολύ διαφορετικό σημείο της μνήμης. Για να βρούμε τη διεύθυνση της system, πρέπει να βρούμε μια διεύθυνση της stdlib που χρησιμοποιείται από το πρόγραμμά μας και μετά να βρούμε το offset της από τη system, το οποίο είναι πάντα σταθερό λόγω του ότι ο κώδικας της stdlib είναι συνεχόμενος. Θα εκμεταλλευτούμε για ακόμα μια φορά το printf της check_auth για να κάνουμε overlook τη μνήμη. Μέσω πειραματισμών με gdb, βρήκαμε (ευτυχώς σχετικά γρήγορα) μια διεύθυνση μνήμης η οποία περιέχει χρήση του stdin. Έπειτα βρήκαμε το offset αυτής της συνάρτησης από τη system.
* Αφού βρήκαμε το offset, κάναμε overlook τη μνήμη που περιείχε την διέυθυνση της stdlib, προσθέσαμε το offset και είχαμε έτοιμη τη διεύθυνση που θέλαμε να στείλουμε το πρόγραμμά μας.
* Είναι σημαντικό να αναφέρουμε ότι σε αυτή την περίπτωση δεν κάνουμε jump σε εντολή που καλεί τη συνάρτηση, αλλά στην αρχή του κώδικα της συνάρτησης. Όταν δοκιμάσαμε να λειτουργήσουμε με τον προηγούμενο τρόπο δεν δούλεψε. Υποψιαζόμαστε ότι είναι λόγω της έλλειψης linkage (δηλαδή, λόγω έλλειψης κλήσης, κάνει απλό jump και όχι jal, άρα δεν αποθηκεύει κάπου το προηγούμενο return address). Οπότε, για να μπορέσει η συνάρτηση να λάβει σωστά το όρισμα, πρέπει να προσθέσουμε και έξτρα 4 bytes στη θέση όπου θα έμπαινε το return address.

**Σχόλιο:** Πρέπει να προσέξουμε, όταν τρέχουμε την εντολή για ip, να ανακατευθύνουμε το αποτέλεσμα σε ένα αρχείο σε κατάλογο που έχουμε δικαιώματα (πχ temp), καθώς κάποιοι κατάλογοι δεν μας το επιτρέπουν (πχ log)!

## Σχόλιο για script
Το script hack.py χρησιμοποιήθηκε 2 φορές στο ερώτημα 4, οπότε είναι σαν template για απόκτηση αρχείων από το server. Μπορεί να χρησιμοποιηθεί για να πάρουμε όλα τα αρχεία του server, αν θέλουμε :)

## Not used
* Χρήση port 443 για να βρούμε την ip των sites (πιθανή τοποθεσία Γιώργου). (https://www.netsparker.com/blog/web-security/exposing-public-ips-tor-services-through-ssl-certificates/)
* "Σπάσιμο" strcmp στο server από το github. Το εγκαταλείψαμε καθώς γίνεται hash σε συγκεκριμένο μέγεθος string, το οποίο δεν προκαλεί overflow.
* strdup exploitation (https://books.google.gr/books?id=XQ6VxBa7bKIC&pg=PA179&lpg=PA179&dq=strdup+exploitation&source=bl&ots=W6VsMc3QeG&sig=ACfU3U3cepP5cnfdzE0181SO8l2S3O1rtA&hl=el&sa=X&ved=2ahUKEwit0uT-q73qAhXO0KQKHSgLDwwQ6AEwDHoECAkQAQ#v=onepage&q=strdup%20exploitation&f=false)
