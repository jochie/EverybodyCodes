#!/usr/bin/perl

# Surely there's a more efficient way :)

use strict;
use warnings;

my $total = 0;
my $min = undef;
my $max = undef;

my @numbers = ();
while (<>) {
    chomp;
    if (!defined($min) || $_ < $min) {
	$min = $_;
    }
    if (!defined($max) || $_ > $max) {
	$max = $_;
    }
    push @numbers, $_;
    $total++;
}

my $avg = int(($min + $max) / 2);
print("$min; $max; $avg; $total\n");

sub calculate_hits {
    my $target = shift;

    my $hits = 0;
    foreach my $number (@numbers) {
	if ($number == $target) {
	    # Skip
	} elsif ($number > $target) {
	    $hits += ($number - $target);
	} else {
	    # $number < $target
	    $hits += ($target - $number);
	}
    }
    return $hits;
}

my $min_hits = undef;
for (my $target = $min; $target <= $max; $target++) {
    my $hits = calculate_hits($target);
    # print("Target $target: Total hits: $hits\n");
    if (!defined($min_hits) || $hits < $min_hits) {
	$min_hits = $hits;
    }
}

print("Minimum number of hits: $min_hits\n");
