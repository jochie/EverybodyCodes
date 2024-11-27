#!/usr/bin/perl

use strict;
use warnings;

my @grid = ();
while (<>) {
    chomp;
    push @grid, $_;
}

sub level {
    my ($row, $col) = @_;

    my $cel = substr($grid[$row], $col, 1);
    if ($cel eq '.' || $cel eq '#') {
	return 0;
    }
    return ord($cel) - ord("0");
}

sub diggable {
    my ($row, $col) = @_;

    my $depth = level($row, $col) + 1;
    my @area = (
	level($row - 1, $col),
	level($row, $col - 1),
	level($row, $col + 1),
	level($row + 1, $col)
	);
    for my $d (@area) {
	if ($depth - $d > 1) {
	    return 0;
	}
    }
    return 1;
}

sub try_to_dig {
    my $dug = 0;
    for (my $r = 0; $r < @grid; $r++) {
	for (my $c = 0; $c < length($grid[$r]); $c++) {
	    my $cel = substr($grid[$r], $c, 1);
	    if ($cel eq '.') {
		next;
	    }
	    if (diggable($r, $c)) {
		$dug++;
		if ($cel eq '#') {
		    substr($grid[$r], $c, 1) = '1';
		} else {
		    substr($grid[$r], $c, 1) = chr(ord($cel)+1);
		}
	    }
	}
    }
    print("Locations dug: $dug\n");
    return $dug;
}

my $total_dug = 0;
while (1) {
    my $dug = try_to_dig();
    if ($dug == 0) {
	last;
    }
    $total_dug += $dug;
    print "$_\n" foreach (@grid);
}
print("Total: $total_dug\n");
