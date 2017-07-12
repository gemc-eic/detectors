use strict;
use warnings;
our %detector;
our %configuration;
our %parameters;

use Getopt::Long;
use Math::Trig;

my $DetectorMother="root";

my $DetectorName = 'det1_tracker_barrel';

my $offset=70.9;

my $offset_inner=40.3;

sub det1_tracker_barrel
{
 my $NUM  = 1;
 my @z    = ($offset_inner);
 my @Rin  = (20);
 my @Rout = (95);
 my @Dz   = (170);
 my @name = (""); 
 my @mother = ("$DetectorMother"); 
 my $mat  = ("Vacuum");

 for(my $n=1; $n<=$NUM; $n++)
 {
    my %detector=init_det();
    $detector{"name"}        = "$DetectorName\_$name[$n-1]";
    $detector{"mother"}      = "$mother[$n-1]" ;
    $detector{"description"} = "$DetectorName\_$name[$n-1]";
    $detector{"pos"}        = "0*cm 0*cm $z[$n-1]*cm";
    $detector{"rotation"}   = "0*deg 0*deg 0*deg";
    $detector{"color"}      = "fff4e7"; 
    $detector{"type"}       = "Tube";
    $detector{"dimensions"} = "$Rin[$n-1]*cm $Rout[$n-1]*cm $Dz[$n-1]*cm 0*deg 360*deg";
    $detector{"material"}   = $mat;
    $detector{"mfield"}     = "no";
    $detector{"ncopy"}      = 1;
    $detector{"pMany"}       = 1;
    $detector{"exist"}       = 1;
    $detector{"visible"}     = 1;
    $detector{"style"}       = 1;
    $detector{"sensitivity"} = "no";
    $detector{"hit_type"}    = "no";
    $detector{"identifiers"} = "no";
     print_det(\%configuration, \%detector);
 }



#--------------- Silicon  --------------------------

 my $NUMS  = 8;
 my @zS    = ($offset_inner,$offset_inner,$offset_inner,$offset_inner,$offset_inner,$offset_inner);
# my @z    = (0,0,0,0);
# my @RinS  = ($Rin, $Rin+1,$Rin+3, $Rin+7,$Rin+11, $Rin+14);
# my @RoutS = ($Rin+0.05,$Rin+1+0.05,$Rin+3+0.05,$Rin+7+0.05,$Rin+11+0.05,$Rin+14+0.05);
 my @nameS = ("OSi1","OSi2","OSi3","OSi4","OSi5","OSi6","OSi7","OSi8"); 
 my @motherS = ("$DetectorMother","$DetectorMother","$DetectorMother","$DetectorMother","$DetectorMother","$DetectorMother"); 
 my $matS  = ("Vacuum");
# my $rotBeam=0.025;
 my $rotBeam=0.0;
# my $NUM  = 2;
# my @z    = ($VTX_offset,$VTX_offset);
# my @z    = (0,0,0,0);
# my @Rin  = (3.00,5.00);
# my @Rout = (3.045,5.045);
# my @Dz   = (90,125);
# my @name = ("1","2"); 
 #my @mother = ("$DetectorMother","$DetectorMother"); 
# my $mat  = ("Air");


 for(my $n=1; $n<=$NUMS; $n++)
 {
    my $RinS=  $Rin[0] +10*($n-1); 
    my $RoutS=  $RinS+0.05; 
    my %detector=init_det();
    $detector{"name"}        = "$DetectorName\_$nameS[$n-1]";
    $detector{"mother"}      = "$mother[0]" ;
    $detector{"description"} = "$DetectorName\_$nameS[$n-1]";
    $detector{"pos"}        = "0*cm 0*cm $offset_inner*cm";
    $detector{"rotation"}   = "0*deg $rotBeam*rad 0*deg";
    $detector{"color"}      = "fbc83c"; 
    $detector{"type"}       = "Tube";
    $detector{"dimensions"} = "$RinS*cm $RoutS*cm $Dz[0]*cm 0*deg 360*deg";
    $detector{"material"}   = $matS;
    $detector{"mfield"}     = "no";
    $detector{"ncopy"}      = 1;
    $detector{"pMany"}       = 1;
    $detector{"exist"}       = 1;
    $detector{"visible"}     = 1;
    $detector{"style"}       = 1;
    $detector{"sensitivity"} = "flux";
    $detector{"hit_type"}    = "flux";
    my $id=61000+$n*100;
    $detector{"identifiers"} = "id manual $id";
     print_det(\%configuration, \%detector);
 }



}
