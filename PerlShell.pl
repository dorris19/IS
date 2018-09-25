use warnings;
use strict;
use IO::File;
use v5.16;


say 'What would you like to test?';
my $test_string = <STDIN>;
chomp $test_string;
my @test_list = split(' ', $test_string);

my $pass_through = join(',', @test_list);

#my $returncode = system("swipl -g 'consult('parser')' -g 'recognize_topdown([that,the,third,angle,of,a,triangle,is,mathStuff])' -t halt 2> /dev/null");
my $first_string = qq{swipl -g 'consult('parser')' -g 'recognize_topdown([};
my $second_string = qq{])' -t halt 2> /dev/null};
my $string_test = join "",$first_string, $pass_through, $second_string;

my $returncode = system($string_test);


if($returncode == 0){
	say 'true!';
}
else{
	say 'false!';
}
