from django.contrib import admin
from .models import (
    Article,
    ArticleElements,
    TagsAll,
    ArticleTags,
    Category,
    SubCategory,
    ElementType,
    Regions,
)


class ElementTypeAdmin(admin.ModelAdmin):
    readonly_fields = ('jinja_name', )
    list_display = ('name', 'display_name', 'jinja_name',)

    ordering = ('display_name',)


class SubCategoryAdminInline(admin.TabularInline):
    model = SubCategory
    list_display = ('name', 'display_name', 'jinja_name',)

    ordering = ('display_name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_name',)
    inlines = (SubCategoryAdminInline,)

    ordering = ('display_name',)


class TagsAllAdmin(admin.ModelAdmin):
    readonly_fields = ('tag_name', )
    list_display = ('name', 'display_name', 'tag_name',)

    ordering = ('display_name',)


class RegionsAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_name',)

    ordering = ('display_name',)


class ArticleElementsAdminInline(admin.TabularInline):
    model = ArticleElements
    readonly_fields = ('article_number', )


class ArticleTagsAdminInline(admin.TabularInline):
    model = ArticleTags
    readonly_fields = ('article_number', )


class ArticleAdmin(admin.ModelAdmin):
    inlines = (ArticleElementsAdminInline, ArticleTagsAdminInline)

    readonly_fields = ('article_number', )

    fields = (
        'article_number',
        'article_category',
        'heading',
        'article_insight',
        'article_image',
        'posted_by',
        'date',
        'source',
        'original_post',
        )

    list_display = ('article_number', 'heading', 'date',)

    ordering = ('-date',)


admin.site.register(Regions, RegionsAdmin)
admin.site.register(TagsAll, TagsAllAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(ElementType, ElementTypeAdmin)
