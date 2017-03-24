use strict;
use warnings;
our %detector;
our %configuration;
our %parameters;

use Getopt::Long;
use Math::Trig;

my $DetectorMother="root";

my $DetectorName = 'det1_tracker_vertex';
my $DetectorNameS = 'det1_tracker_vtxSupp';

my $offset=70.9;

my $VTX_offset=5;

my $Beampipe_outer=3.32;

sub det1_tracker_vertex
{
    my $Rin=$Beampipe_outer+0.5;


#--------------- VERTEX Support --------------------------

 my $NUMS  = 3;
 my @zS    = ($VTX_offset,$VTX_offset,$VTX_offset);
# my @z    = (0,0,0,0);
 my @RinS  = ($Rin, $Rin+1,$Rin+2);
 my @RoutS = ($Rin+0.05,$Rin+1+0.05,$Rin+2+0.05);
 my @DzS   = (20,22,26);
 my @nameS = ("1","2","3"); 
 my @motherS = ("$DetectorMother","$DetectorMother","$DetectorMother"); 
 my $matS  = ("Vacuum");
 my $rotBeam=0.025;
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


    my %detector=init_det();
    $detector{"name"}        = "$DetectorNameS\_$nameS[$n-1]";
    $detector{"mother"}      = "$motherS[$n-1]" ;
    $detector{"description"} = "$DetectorNameS\_$nameS[$n-1]";
    $detector{"pos"}        = "0*cm 0*cm $VTX_offset*cm";
    $detector{"rotation"}   = "0*deg $rotBeam*rad 0*deg";
    $detector{"color"}      = "fbc83c"; 
    $detector{"type"}       = "Tube";
    $detector{"dimensions"} = "$RinS[$n-1]*cm $RoutS[$n-1]*cm $DzS[$n-1]*cm 0*deg 360*deg";
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

#----------------------Silicon ladders ---------------------
#---- number of layers------
my $NUML  = 3;  
# my $NUM  = 13;
# my @z    = (0,0,0,0);
 my $phi =0;
 my $deltaphi =0;
 my $NUM  = 0;

# my @mother = ("$DetectorMother","$DetectorMother","$DetectorMother","$DetectorMother"); 
 my $mother = ("$DetectorMother");
 my $mat  = ("G4_Si");
 my  @posX    = (0,0,0,0,0,0,0,0,0,0,0,0,0);
 my  @posY    = (0,0,0,0,0,0,0,0,0,0,0,0,0);
 my  @posZ    = (0,0,0,0,0,0,0,0,0,0,0,0,0);

 for(my $l=1; $l<=$NUML; $l++)
 {

      my $Hx  = 1.;
      my $Hy = 0.03;
      my $Hz   = $DzS[$l-1];  

     my $z    = $DzS[$l-1]/2;
     my $x    = $RoutS[$l-1]+0.1;
     my $y    = $RoutS[$l-1]+0.1;
     if ($l==1) { 
	  $NUM  = 13;
	  $deltaphi=30; 
     }	elsif ($l==2)  {
	 $NUM  = 14;
	 $deltaphi=26;
     } else {
	 $NUM  = 18;
	 $deltaphi=20;
	 
     }
      for(my $n=1; $n<=$NUM; $n++)
     {
	 my $y1=-($Hx/2);
	 $phi=($n-1)*($deltaphi)*3.14159/180.;
	 $posX[$n-1]=$x*cos($phi);
	 $posY[$n-1]=$y*sin($phi);
	 $posZ[$n-1]=$VTX_offset;
	 my $Rotation=(90-$phi*180/3.1415+7);
#     my $Rotation=0;
	 print "$n posX: cos($phi)  $phi -$Hx/2  $x $posX[$n-1] \n";
	 print "$n posY: cos($phi) $phi   $y $posY[$n-1] \n";
	 
	 
	 my %detector=init_det();
	 my $name =("Vertex\_$l\_$n");
	 print "detector name  $name ";
	 $detector{"name"}        = "$name";
	 $detector{"mother"}      = "$mother" ;
	 $detector{"description"} = "$name";
	 $detector{"pos"}        = "$posX[$n-1]*cm $posY[$n-1]*cm $posZ[$n-1]*cm";
	 $detector{"rotation"}   = "0*deg $rotBeam*rad $Rotation*deg";
#	 $detector{"color"}      = "502a60"; 
#	 $detector{"color"}      = "461d90"; 
	 $detector{"color"}      = "8051d6"; 
	 #   $detector{"type"}       = "Tube";
	 #   $detector{"dimensions"} = "$Rin[$n-1]*cm $Rout[$n-1]*cm $Dz[$n-1]*cm 0*deg 360*deg";
	 $detector{"type"}       = "Box";
	 $detector{"dimensions"} = "$Hx*cm $Hy*cm $Hz*cm";
	 $detector{"material"}   = $mat;
	 $detector{"mfield"}     = "no";
	 $detector{"ncopy"}      = 1;
	 $detector{"pMany"}       = 1;
	 $detector{"exist"}       = 1;
	 $detector{"visible"}     = 1;
	 $detector{"style"}       = 1;
	 $detector{"sensitivity"} = "flux";
	 $detector{"hit_type"}    = "flux";
	 my $id=50000+$l*100+$n;
	 $detector{"identifiers"} = "id manual $id";
	 print_det(\%configuration, \%detector);
     }
 }


}
