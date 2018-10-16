use Lingua::EN::Tagger;
use warnings;
use strict;
use v5.16;

my $p = new Lingua::EN::Tagger;
my $text = "Hello I would like to speak to your manager please."; 
my $tagged_text = $p->add_tags($text);
my %word_list = $p->get_words($text);
my $readable_text = $p->get_readable($text);
my $nouns = $p->get_nouns($tagged_text);
my $words = $p->get_words($text);
say $tagged_text;
