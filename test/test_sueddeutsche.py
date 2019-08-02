from hamcrest import assert_that, equal_to, contains_string

from crawler.sueddeutsche import SueddeutscheArticle


class TestSueddeutsche(object):

    def test_crawled_article_has_correct_headline(self):
        article = SueddeutscheArticle('https://www.sueddeutsche.de/sport/basketball-wm-roedl-deutschland-1.4549039')
        assert_that(article.headline, equal_to("Selbst Nowitzki schwärmt"))

    def test_crawled_article_has_correct_subheadline(self):
        article = SueddeutscheArticle('https://www.sueddeutsche.de/sport/basketball-wm-roedl-deutschland-1.4549039')
        assert_that(article.sub_headline, equal_to("Deutscher Kader für Basketball-WM"))

    def test_crawled_article_has_correct_and_cleaned_body(self):
        article = SueddeutscheArticle('https://www.sueddeutsche.de/sport/basketball-wm-roedl-deutschland-1.4549039')
        expected_text_parts = [
            "Der unverwüstliche Dirk Nowitzki wird auch bei der kommenden Basketball-WM in China wieder im Einsatz sein, allerdings nicht mehr für die deutsche Nationalmannschaft - aus der ist er ja schon vor vier Jahren zurückgetreten, nach der Heim-EM in Berlin. Im vergangenen Frühjahr hat der mittlerweile 41-Jährige seine Profikarriere nach 21 Jahren bei den Dallas Mavericks dann komplett beendet, aber so abrupt will er sich nun auch wieder nicht verabschieden von seinem Sport. Also hat er sich gern einspannen lassen als weltweiter WM-Botschafter, so kann er aus der Nähe noch mitverfolgen, was seine Nachfolger treiben. \"Wir haben da eine super Truppe\", findet Nowitzki, \"ich glaube, es ist sogar die tiefste, die die Nationalmannschaft je hatte.\"",
            "Bundestrainer Henrik Rödl hatte jedenfalls eine noch nie dagewesene Auswahl bei der Nominierung seines vorläufigen WM-Aufgebots, das er am Donnerstag in Hamburg präsentierte. Mit 16 Spielern startet der 50-Jährige am Montag in Trier in die Vorbereitung, aber bloß zwölf darf er beim Turnier in China (31. August bis 15. September) einsetzen. Rödl sprach von einem \"sehr, sehr spannenden Kader\" und versicherte: \"Wir haben vor niemandem Angst. Wir werden mit breiter Brust überall reingehen. Wie weit uns das trägt, wird sich dann zeigen.\"",
            "Rödl stehen fünf Akteure aus der amerikanischen Profiliga NBA zur Verfügung, so viele wie keinem Bundestrainer vor ihm. Die etablierten Profis hatte er von vornherein gesetzt - Spielmacher Dennis Schröder (Oklahoma City Thunder) sowie die Flügelspieler Maxi Kleber (Dallas Mavericks) und Daniel Theis (Boston Celtics). Dabei soll vor allem Schröder das Team anführen. \"Er ist auf seiner Position einer der Besten der Welt\", sagt Rödl: \"Er hat eine Qualität, die unseren Spielstil prägen wird. Er ist der Mann, der sehr, sehr wichtig ist für uns.",
            "Dazu kommen nun die NBA-Neulinge Isaac Bonga und Moritz Wagner (beide gerade von den Los Angeles Lakers zu den Washington Wizards gewechselt), allerdings ohne Garantie auf einen Stammplatz, wie Rödl mitgeteilt hatte: \"Sie müssen sich noch beweisen.\" Zwei Jahre NBA-Erfahrung bei den Chicago Bulls hat im Übrigen auch Paul Zipser, der zuletzt in der spanischen Liga war und aktuell vereinslos ist.",
        ]

        for part in expected_text_parts:
            assert_that(article.body, contains_string(part))
