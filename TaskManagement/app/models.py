from django.db import models

from users.models import User


class Item(models.Model):
    """
    データ定義クラス
      各フィールドを定義する
    参考：
    ・公式 モデルフィールドリファレンス
    https://docs.djangoproject.com/ja/2.1/ref/models/fields/
    """

    # 題目、選択式
    study_choice = (
        (1, 'WEBサイト'),
        (2, 'WEBアプリ'),
        (3, 'WEBサービス'),
        (4, 'ios/Androidアプリ'),
        (5, 'システム'),
        (6, 'AI関連'),
        (7, 'RPA'),
        (8, '資格'),
    )

    study_choice = models.IntegerField(
        verbose_name='題目',
        choices=study_choice,
        blank=True,
        null=True,
    )

    # タイトル・項目
    title = models.CharField(
        verbose_name='タイトル',
        max_length=20,
        blank=True,
        null=True,
    )

    # メモ
    naiyou = models.TextField(
        verbose_name='内容',
        blank=True,
        null=True,
    )


    # チェックリスト
    do_check = models.BooleanField(
        verbose_name='チェックリスト',
    )

    # 行う日付
    do_date = models.DateField(
        verbose_name='する日',
        blank=True,
        null=True,
    )

    # 以下、管理項目

    # 作成者(ユーザー)
    #   以下管理画面
    created_by = models.ForeignKey(
        User,
        verbose_name='作成者',
        blank=True,
        null=True,
        related_name='CreatedBy',
        on_delete=models.SET_NULL,
        editable=False,
    )

    # 作成時間
    created_at = models.DateTimeField(
        verbose_name='作成時間',
        blank=True,
        null=True,
        editable=False,
    )

    # 更新者(ユーザー)
    updated_by = models.ForeignKey(
        User,
        verbose_name='更新者',
        blank=True,
        null=True,
        related_name='UpdatedBy',
        on_delete=models.SET_NULL,
        editable=False,
    )

    # 更新時間
    updated_at = models.DateTimeField(
        verbose_name='更新時間',
        blank=True,
        null=True,
        editable=False,
    )

    def __str__(self):
        """
        リストボックスや管理画面での表示
        """
        return self.sample_1

    class Meta:
        """
        管理画面でのタイトル表示
        """
        verbose_name = 'MAMEZOU'
        verbose_name_plural = 'MAMEZOU'
