use warnings;
use strict;
use IO::File;
use v5.16;

my $returncode = system("swipl -g 'consult('parser')' -g 'recognize_topdown([that,the,third,angle,of,a,triangle,is,mathStuff])' -t halt 2> /dev/null");


if($returncode == 0){
	say 'true!';
}
else{
	say 'false!';
}
