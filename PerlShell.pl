use warnings;
use strict;
use IO::File;
use v5.16;

#Take user input, remove formatting, and split to an array
say 'What would you like to test?';
my $test_string = <STDIN>;
chomp $test_string;
my @test_list = split(' ', $test_string);

#Turn array into a string for passing to prolog

my $pass_through = join(',', @test_list);

#Format string for shell use

my $first_string = qq{swipl -g 'consult('prolog_parser')' -g 'recognize_topdown([};
my $second_string = qq{])' -t halt 2> /dev/null};
my $string_test = join "",$first_string, $pass_through, $second_string;


#Run command, if no errors are produced, statement is true.
#If errors do occur, prolog either found something wrong with the input
#or it returned false - we assume false here

my $returncode = system($string_test);


if($returncode == 0){
	say 'true!';
}
else{
	say 'false!';
}
