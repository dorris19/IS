use strict;
use warnings;
use diagnostics;

use feature 'say';

use feature "switch";

use v5.16;

#basic assignment of variables
my $house_color = "green";
my $name = "Dylan";
my ($address, $dorm) = ("1189 Beall Ave", "Brush Hall");
#qq represents double quotes, removes need to exit quotes within 
#content
my $my_info = qq{$name lives at $address in $dorm.\n};
say $my_info;

#Easy multiline output using <<"END"

my $multiline = <<"END";
This is a
ton of text
that I can easily
split by line
END

say $multiline;

#Easy value swapping of variables
my $older_man = "Thomas";
my $younger_man = "Jim";

say "$older_man is currently the older man, and $younger_man is the 
younger";

($older_man, $younger_man) = ($younger_man, $older_man);

say "Now, $older_man is the older man, while $younger_man is the 
younger";

#basic if statement with else if
if($older_man eq "Thomas"){
   say "It looks like something went wrong in our records, Jim is older 
than you!";
}
elsif($older_man eq "Jim"){
   say "Hello Jim, sorry about the mix up earlier."
}

#basic input
say "Tell us what Phillip really thinks!";

#chomp removes trailing characters from variable (in this case, new 
#line)
chomp (my $phillip_wells = <STDIN>);

say qq{Phillip says "$phillip_wells!"};

#double variable assignment, which I was explicitly told not to do
#doesn't work quite as described, may look into for fun
#my $gianni = "FTL";
#my $FTL = 8;

#say "$$gianni";
