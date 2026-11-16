:title: CAPITULUM XII.7 — QUOT PARIA CONICULORUM (THE RABBIT PROBLEM)
:layout: book
:order: 12
:tracks: English: cap_12-en | Latin: cap_12-la | Summary: cap_12-summary | Notes: cap_12-notes
:folio: boncompagni_1857_vol1_liber_abbaci:0289
:excerpt: The rabbit problem of Liber Abbaci Chapter XII, introducing the Fibonacci recurrence sequence and its convergence to the golden ratio phi.

.. _cap-12-en:
.. _unit-5-rabbits-en:
.. _liber-abbaci-cap12-en:

CAPITULUM XII.7 — QUOT PARIA CONICULORUM (THE RABBIT PROBLEM)
=============================================================

.. rubric:: *The Rabbit Problem, the Recurrence Sequence F(n+1) = F(n) + F(n-1), and the Asymptotic Limit to the Divine Proportion*

**Source Text**: :cite:`boncompagni:1857` (*Il Liber Abbaci, Vol. I, pp. 283–284 · fol. 124r*) · :ref:`Latin (1202/1228 / Boncompagni 1857) <cap-12-la>` · :ref:`Summary <cap-12-summary>` · :ref:`GEOMETOR Notes <cap-12-notes>`

----

.. _cap-12-rabbits-en:

.. folio:: boncompagni_1857_vol1_liber_abbaci:0289
   :page: 283–284

How Many Pairs of Rabbits Are Bred in One Year from a Single Pair
-----------------------------------------------------------------

*Latin Locus*: :ref:`Quot Paria Coniculorum in Uno Anno (Vol. I, pp. 283–284) <cap-12-la>` · *Commentary*: :ref:`Notes on Cassini's Identity & Golden Convergence <cap-12-notes>`

.. enunciation::

   How many pairs of rabbits are bred in one year from a single pair (*Quot paria coniculorum in uno anno ex uno pario germinentur*).

A certain man placed one pair of rabbits in a place surrounded on all sides by a wall, to find how many pairs would be bred from it in one year: when by nature every mature pair produces another pair every month, and each newborn pair begins to bear in the second month after its birth.

Because the aforesaid pair breeds in the first month, you double it: there will be **$2$ pairs** in one month.

Of these, one—namely the first pair—breeds in the second month; and thus there are in the second month **$3$ pairs**.

Of these, in one month two pairs are pregnant; and in the third month $2$ pairs of rabbits are bred; and thus there are **$5$ pairs** in that month.

Of these, in that month $3$ pairs are pregnant; and there are in the fourth month **$8$ pairs**.

Of these, $5$ pairs breed another $5$ pairs; which added to the $8$ pairs make **$13$ pairs** in the fifth month.

Of these, the $5$ pairs which were bred in that month do not conceive in that same month, but the other $8$ pairs are pregnant; and thus there are in the sixth month **$21$ pairs**.

.. folio:: boncompagni_1857_vol1_liber_abbaci:0290
   :page: 284

Which added with the $13$ pairs that are bred in the seventh month, there will be in it **$34$ pairs**;

with which added the $21$ pairs that are bred in the eighth month, there will be in it **$55$ pairs**;

with which added the $34$ pairs that are bred in the ninth month, there will be in it **$89$ pairs**;

with which added again the $55$ pairs that are bred in the tenth month, there will be in it **$144$ pairs**;

with which added again the $89$ pairs that are bred in the eleventh month, there will be in it **$233$ pairs**;

with which also added the $144$ pairs that are bred in the last month, there will be **$377$ pairs**.

And so many pairs did the aforesaid pair bring forth in the aforesaid place at the head of one year.

.. list-table:: Marginal Generation Table from Codex Magliabechiano (fol. 124r)
   :header-rows: 1
   :widths: 30 20 50

   * - Month / Degree
     - Pairs ($F_n$)
     - Cumulative Pairs Generated
   * - *Initium*
     - **$1$**
     - Original pair placed in enclosed court
   * - *Primus*
     - **$2$**
     - Original pair produces 1st offspring pair
   * - *Secundus*
     - **$3$**
     - Original pair produces 2nd offspring pair
   * - *Tertius*
     - **$5$**
     - 1st offspring pair matures and produces
   * - *Quartus*
     - **$8$**
     - 3 mature pairs produce 3 new pairs
   * - *Quintus*
     - **$13$**
     - 5 mature pairs produce 5 new pairs
   * - *Sextus*
     - **$21$**
     - 8 mature pairs produce 8 new pairs
   * - *Septimus*
     - **$34$**
     - 13 mature pairs produce 13 new pairs
   * - *Octavus*
     - **$55$**
     - 21 mature pairs produce 21 new pairs
   * - *Nonus*
     - **$89$**
     - 34 mature pairs produce 34 new pairs
   * - *Decimus*
     - **$144$**
     - 55 mature pairs produce 55 new pairs
   * - *Undecimus*
     - **$233$**
     - 89 mature pairs produce 89 new pairs
   * - *Duodecimus*
     - **$377$**
     - 144 mature pairs produce 144 new pairs

.. qed::

   You can indeed see in this margin how we have operated, namely that we joined the first number with the second, videlicet $1$ with $2$; and the second with the third; and the third with the fourth; and the fourth with the fifth, and so in order, until we joined the tenth with the eleventh, videlicet $144$ with $233$; and we had the sum of the aforesaid rabbits, videlicet **$377$**; **and thus you could do in order for an infinite number of months** (*et sic posses facere per ordinem de infinitis numeris mensibus*).
