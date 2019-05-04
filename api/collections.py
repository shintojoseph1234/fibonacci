
from mongoengine import *



class MyModel(Document):

  name      = StringField()
  meta      = {'allow_inheritance': True }


############## Questionnaire API

class QuestionAnswer(EmbeddedDocument):

    question_code       = StringField(required=True)
    answer_code         = StringField(required=True)
    answer_value        = StringField(required=False, null=True)


class Questionnaire(Document):

    customer_id         = StringField(required=True)
    question_answer     = ListField(EmbeddedDocumentField('QuestionAnswer'), required=True)


################## Generate Recommendations API

class Goals(EmbeddedDocument):

    goal_id             = StringField(required=True)
    goal_priority       = StringField(required=True)
    initial_amount      = FloatField(required=True)
    monthly_amount      = FloatField(required=True)
    goal_amount         = FloatField(required=True)
    goal_duration       = FloatField(required=True)
    loss_threshold      = FloatField(required=True)

class Generate(Document):

    customer_id         = StringField(required=True)
    risk_score          = FloatField(required=True)
    goals               = ListField(EmbeddedDocumentField('Goals'), required=True)

############### Risk Score API
class CurrentPortfolio(EmbeddedDocument):

    id                = StringField(required=True)
    assetId           = StringField(required=True)
    assetClass        = StringField(required=True)
    name              = StringField(required=True)
    percentage        = IntField(required=True)


class RiskQuestionAnswer(EmbeddedDocument):

    question_code       = StringField(required=True)
    answer_code         = StringField(required=False, null=True)
    answer_value        = StringField(required=False, null=True)

class RiskScore(Document):

    customer_id         = StringField(required=True)
    question_answer     = ListField(EmbeddedDocumentField('RiskQuestionAnswer'), required=True)
    current_portfolio   = ListField(EmbeddedDocumentField('CurrentPortfolio'), required=False, null=True)


############## loss simulation API

class LossSimulation(Document):

    loss_threshold      = FloatField(required=True)
    time_period         = FloatField(required=True)
    portfolio           = ListField(required=False, null=True)


############ HistoricalSimulation API

class HistoricalSimulation(Document):

    from_date               = StringField(required=True)
    to_date                 = StringField(required=True)
    asset_class             = ListField(required=False, null=True)
    recommended_portfolio   = DictField(required=False, null=True)
    model_portfolio_1       = DictField(required=False, null=True)
    model_portfolio_2       = DictField(required=False, null=True)

############# Create Model Portfolio API

class CreatedPortfolio(EmbeddedDocument):

    GOLD                = FloatField(required=True)
    BOND                = FloatField(required=True)
    CASH                = FloatField(required=True)
    EQUITY_LARGE_CAP    = FloatField(required=True)
    EQUITY_SMALL_CAP    = FloatField(required=True)


class ModelPortfolio(Document):

    user_id             = StringField(required=True)
    goal_id             = StringField(required=True)
    initial_amount      = FloatField(required=True)
    monthly_amount      = FloatField(required=True)
    goal_amount         = FloatField(required=True)
    time_period         = FloatField(required=True)
    goal_priority       = StringField(required=True)
    model_portfolio     = DictField(required=True)



############# Save and Confirm

class SaveAndConfirm(Document):

    user_id             = StringField(required=True)
    goal_id             = StringField(required=True)
    initial_amount      = FloatField(required=True)
    monthly_amount      = FloatField(required=True)
    goal_amount         = FloatField(required=True)
    goal_duration       = FloatField(required=True)
    probability         = FloatField(required=True)
    risk_score          = FloatField(required=True)
    portfolio_type      = StringField(required=True)
    asset_allocation    = DictField(required=True)
    securities_data     = ListField(required=True)


############# Stress Test

class Stress(Document):

    asset_allocation    = DictField(required=False, null=True)
    portfolio           = ListField(required=False, null=True)
    crash               = ListField(required=True)

########## sprint 5 ###############################

############## Questionnaire API

class QuestionAnswerLite(EmbeddedDocument):

    question_code       = StringField(required=True)
    answer_code         = StringField(required=False, null=True)
    answer_value        = StringField(required=False, null=True)


class QuestionnaireLite(Document):

    customer_id         = StringField(required=True)
    question_answer     = ListField(EmbeddedDocumentField('QuestionAnswerLite'), required=True)


############ Risk Score Lite API

class RiskQuestionAnswerLite(EmbeddedDocument):

    question_code       = StringField(required=True)
    answer_code         = StringField(required=False, null=True)
    answer_value        = StringField(required=False, null=True)

class RiskScoreLite(Document):

    user_id             = StringField(required=True)
    customer_id         = StringField(required=True)
    current_portfolio   = ListField(required=False, null=True)
    question_answer     = ListField(EmbeddedDocumentField('RiskQuestionAnswerLite'), required=False,  null=True)

########### Portfolio score API

class CurrentPortfolioLite(EmbeddedDocument):

    percentage       = StringField(required=True)
    assetClass       = StringField(required=True)

class PortfolioScoreLite(Document):

    current_portfolio     = ListField(EmbeddedDocumentField('CurrentPortfolioLite'), required=True)

########### Risk Deviation API

class RiskDeviation(Document):

    customer_ids  = ListField(required=True)

########### File Upload API

class FileUpload(Document):

    user_id         = StringField(required=True)
    files           = ListField(required=True)


########### Create stress test


class RscoreStressAssetAllocation(EmbeddedDocument):

    id              = StringField(required=True)
    name            = StringField(required=True)
    assetClass      = StringField(required=True)
    percentage      = IntField(required=True)


class CreateStress(Document):

    asset_allocation    = ListField(EmbeddedDocumentField('RscoreStressAssetAllocation'), required=True,  null=False)
    shock_p             = IntField(required=True)
    rise_fall           = StringField(required=True)
    risk_factor_id      = StringField(required=True)
    risk_factor         = StringField(required=True)


########################### Riskonaut Validations

########### Register User
class Register(Document):

    Name         = StringField(required=True)
    Email        = StringField(required=True)
    Password     = StringField(required=True)
    MobileNumber = StringField(required=True)
    Pincode      = StringField(required=True)

########### Login
class Login(Document):

    Email        = StringField(required=True)
    Password     = StringField(required=True)


########### Reset Password
class ResetPassword(Document):

    Email           = StringField(required=True)
    NewPassword     = StringField(required=True)
    CurrentPassword = StringField(required=True)


########### Forgot Password
class ForgotPassword(Document):

    Email  = StringField(required=True)


########### Add new client Password
class AddClient(Document):

    Name        = StringField(required=True)
    Email       = StringField(required=True)
    Mobile      = StringField(required=True)
    DOB         = StringField(required=True)
    Pincode     = StringField(required=True)
    regionalID  = StringField(required=True)
    CreatedBy   = StringField(required=True)


########### Resend Link
class ResendLink(Document):

    Name        = StringField(required=True)
    Email       = StringField(required=True)
    Mobile      = StringField(required=True)
    DOB         = StringField(required=True)
    Pincode     = StringField(required=True)
    CreatedBy   = StringField(required=True)


########### Resend Link
class CustomerDetails(Document):

    user_id        = StringField(required=True)
    customer_id    = StringField(required=True)


########### GeneratePdf
class GeneratePdf(Document):

    user_id        = StringField(required=True)
    customer_id    = StringField(required=True)


########### RecalculatePortfolio
class RecalculatePortfolio(Document):

    user_id             = StringField(required=True)
    customer_id         = StringField(required=True)
    current_portfolio   = ListField(required=False, null=True)
