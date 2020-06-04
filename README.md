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


## Not used
* Χρήση port 443 για να βρούμε την ip των sites (τοποθεσία Γιώργου). (https://www.netsparker.com/blog/web-security/exposing-public-ips-tor-services-through-ssl-certificates/)
* "Σπάσιμο" strcmp στο server από το github. Το εγκαταλείψαμε καθώς γίνεται hash σε συγκεκριμένο μέγεθος string, το οποίο δεν προκαλεί overflow.
