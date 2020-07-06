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

## Not used
* Χρήση port 443 για να βρούμε την ip των sites (τοποθεσία Γιώργου). (https://www.netsparker.com/blog/web-security/exposing-public-ips-tor-services-through-ssl-certificates/)
* "Σπάσιμο" strcmp στο server από το github. Το εγκαταλείψαμε καθώς γίνεται hash σε συγκεκριμένο μέγεθος string, το οποίο δεν προκαλεί overflow.
