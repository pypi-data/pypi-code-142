from io import StringIO
from unittest import TestCase

from main import comment_to_tickets, gather_stats, Ticket, raw_stats_line_to_tuple

params = [
    ("Pull request #60: RD-6759 at a1 to bfs", {"RD-6759"}),
    ("Pull request #60: RD-6759 RD-6759 at a1 to bfs", {"RD-6759", "RD-6759"}),
    ("RD-6758 RD-6759 at a1 to bfs", {"RD-6758", "RD-6759"}),
    ("RD-6758 at a1 to bfs", {"RD-6758"}),
    ("RD-6758: at a1 to bfs", {"RD-6758"}),
    ("RD-6758: GSG-50 at a1 to bfs", {"RD-6758", "GSG-50"}),
]


class Test(TestCase):
    def test_comment_to_tickets(self):
        for comment, expected_tickets in params:
            with self.subTest():
                self.assertEqual(expected_tickets, comment_to_tickets(comment))

    def test_main(self):
        test_input = StringIO()
        test_input.write(
            """<end>
<start>
a6d9fac6fa4a6ee0dc6332206048126fbbafad8d
RD-3549 introduce firs bird - wsdl2java generation, controllers, properties, services
<br>

64	2	pom.xml
1	1	src/main/java/eu/dimoco/hub/route/{ => at}/a1/Application.java
14	0	src/main/java/eu/dimoco/hub/route/at/a1/domain/config/AtA1Properties.java
<end>
<start>
ee3acbcc4a6f3310f47614f6c781293fd7e8223a
RD-3549 initial revision
<br>

26	0	.gitignore
5	0	src/test/resources/bootstrap.yml
"""
        )
        test_input.seek(0)

        stats: dict[str, Ticket] = gather_stats(test_input)

        expected_ticket = Ticket("RD-3549")
        expected_ticket.add_stats((64 + 1 + 14 + 26 + 5, 2 + 1 + 0 + 0 + 0))

        self.assertDictEqual({"RD-3549": expected_ticket}, stats)

    def test_main2(self):
        test_input = StringIO()
        test_input.write(
            """<end>
<start>
824b399b90cc3b01a7def0aafa668f7277774a07
RD-6797 Update route-parent version to latest
<br>

2	2	pom.xml
<end>
<start>
96489c8fd9f1cc2271dc19f4a196f5ecf86d0793
RD-6797 Update route-parent version to latest
<br>

2	2	pom.xml
<end>
<start>
a2c5408df98c1059a29dfec87e4a678bf4b93de3
RD-6810 Update route-parent version to latest
<br>

2	2	pom.xml
<end>
<start>
608fa070aa1de455ab42024cf19907f7df38905d
RD-6812 Update route-parent version to latest
<br>

2	2	pom.xml
<end>
<start>
202cc6ee4737bcccff09acbb13d7b1d183b6a87d
Pull request #60: RD-6759 at a1 identify route service does not report subscriptionid to bfs
<br>
<end>
<start>
586709c4c41e7da077a420a8ec03133003999c76
RD-6759 set the setConnectionCreditProviderSubscriptionId1s and add assertions
<br>

1	2	src/main/java/eu/dimoco/hub/route/at/a1/domain/identify/Identify.java
0	15	src/test/java/eu/dimoco/hub/route/at/a1/IntegrationTest.java
0	2	src/test/java/eu/dimoco/hub/route/at/a1/domain/identify/IdentifyTest.java
0	119	src/test/java/eu/dimoco/hub/route/at/a1/util/AsCp.java
"""
        )
        test_input.seek(0)

        stats: dict[str, Ticket] = gather_stats(test_input)

        expected_ticket6797 = Ticket("RD-6797")
        expected_ticket6797.add_stats((2, 2))
        expected_ticket6797.add_stats((2, 2))
        expected_ticket6810 = Ticket("RD-6810")
        expected_ticket6810.add_stats((2, 2))
        expected_ticket6812 = Ticket("RD-6812")
        expected_ticket6812.add_stats((2, 2))
        expected_ticket6759 = Ticket("RD-6759")
        expected_ticket6759.add_stats((1, 2 + 15 + 2 + 119))
        self.assertDictEqual(
            {
                "RD-6797": expected_ticket6797,
                "RD-6810": expected_ticket6810,
                "RD-6812": expected_ticket6812,
                "RD-6759": expected_ticket6759,
            },
            stats,
        )

    def test_raw_stats_line_to_tuple(self):
        actual = raw_stats_line_to_tuple("64	2	pom.xml\n")

        self.assertEqual((64, 2), actual)
