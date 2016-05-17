has_hair(tiger).
has_hair(cheetah).
has_hair(lion).
has_hair(zebra).
has_hair(horse).
has_hair(dog).
has_hair(cat).
has_hair(human).
has_hair(cow).

gives_milk(platipus).
gives_milk(tiger).
gives_milk(cheetah).
gives_milk(lion).
gives_milk(zebra).
gives_milk(horse).
gives_milk(dog).
gives_milk(cat).
gives_milk(human).
gives_milk(cow).
is_eats_meat(tiger).
is_eats_meat(cheetah).
is_eats_meat(lion).
is_eats_meat(dog).
is_eats_meat(cat).
is_eats_meat(human).

has_pointed_teeth(tiger).
has_pointed_teeth(lion).
has_pointed_teeth(dog).
has_pointed_teeth(cat).
has_claws(tiger).
has_claws(lion).
has_claws(dog).

has_forword_eyes(human).
has_forword_eyes(cat).
has_forword_eyes(dog).
has_forword_eyes(lion).
has_forword_eyes(tiger).

has_hooves(cow).
has_hooves(horse).
has_hooves(zebra).

chews_cud(cow).

has_tawny_color(tiger).
has_tawny_color(cheetah).
has_tawny_color(lion).

has_dark_spots(cheetha).
has_dark_spots(cat).
has_dark_spots(dog).

has_black_strips(tiger).
has_black_strips(zebra).

has_long_neck(giraffe).

is_carnivorous(Y) :- is_eats_meat(Y),has_pointed_teeth(Y),has_claws(Y),has_forword_eyes(Y)
is_mammal(X) :- gives_milk(X),has_hair(X).
is_ungulate(Z) :- is_mammal(Z),has_hooves(Z);chews_cud(Z).
is_cheetah(S) :- is_mammal(S),is_carnivorous(S),has_tawny_color(S),has_dark_spots(S).
is_tiger(A) :-  is_mammal(A),is_carnivorous(A),has_tawny_color(A),has_black_strips(A).
is_girffe(T) :- is_ungulate(T),has_dark_spots(T),has_long_neck(T).
is_zebra(B) :- is_ungulate(B),has_black_strips(B).
