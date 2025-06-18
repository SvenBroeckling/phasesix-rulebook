### PhaseSix and Tirakans Reiche Rulebook

These documents are the source for the role-playing games PhaseSix and Tirakans Reiche.

The documents contain markdown sources enriched with django template tags and filters. They are suitable to be rendered inside the [PhaseSix](https://github.com/SvenBroeckling/phasesix) rpg platform.

The rendering process provides a WorldBook instance with the following variables:

```python
class WorldBook(models.Model, metaclass=TransMeta):
    world = models.ForeignKey("worlds.World", on_delete=models.CASCADE)
    book = models.ForeignKey("rulebook.Book", on_delete=models.CASCADE)
    pdf_de = models.FileField(
        gt("PDF german"), upload_to="rulebook_pdf", blank=True, null=True
    )
    pdf_en = models.FileField(
        gt("PDF english"), upload_to="rulebook_pdf", blank=True, null=True
    )

    disabled_chapters = models.ManyToManyField("rulebook.Chapter", blank=True)

    book_title = models.CharField(gt("book title"), max_length=80)
    book_claim = models.CharField(gt("book claim"), max_length=80)
    book_title_image = models.ImageField(
        gt("book title image"), upload_to="rulebook_title_images", max_length=256
    )
    book_website = models.URLField(gt("book website"), blank=True, null=True)

    @property
    def identifier(self):
        return self.world.identifier


class World(models.Model, metaclass=TransMeta):
    name = models.CharField(_("name"), max_length=120)
    slug = models.SlugField(_("slug"), max_length=220, unique=True, null=True)
    brand_name = models.CharField(_("Brand name"), max_length=80)
    brand_claim = models.CharField(
        _("Brand claim"), max_length=80, null=True, blank=True
    )
    brand_logo = models.ImageField(
        _("Brand Logo"), max_length=256, null=True, blank=True, upload_to="brand_logos"
    )

    description_1 = models.TextField(_("description 1"), blank=True, null=True)
    description_2 = models.TextField(_("description 2"), blank=True, null=True)
    description_3 = models.TextField(_("description 3"), blank=True, null=True)

    is_active = models.BooleanField(_("is active"), default=True)
    is_default = models.BooleanField(_("is default"), default=False)
    info_name_cm = models.CharField(_("Name for centimeter"), max_length=20, default="cm")
    info_name_kg = models.CharField(_("Name for kilogram"), max_length=20, default="kg")

    @property
    def identifier(self):
        return self.extension.identifier
```
