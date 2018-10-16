use lib 'home/usr/perl5';
use strict;
use warnings;
use AI::Prolog;
use File::Slurp;
use Data::Dumper;
use v5.16;

#Take user input for question to be proved
say 'What would you like to test?';
my $test_string = <STDIN>;
chomp $test_string;

#Read in parser file to put rules in
my $database = read_file('parser.pl');

#define prolog based on our read in database
my $prolog = AI::Prolog->new($database);

#Would usually be $test_string, but for testing currently is as defined
$prolog->query("prove that the third angle of a triangle is mathStuff.");

#puts out answer
while (my $result = $prolog->results) {
	print Dumper $result;
}
#if what we had was a valid question, we work with it
#Will probably need a new database to do determinations of what axioms to use
