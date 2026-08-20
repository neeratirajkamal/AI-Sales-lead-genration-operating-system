from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional, Dict, Any
from enum import Enum
from datetime import datetime

class PresenceType(str, Enum):
    legal_entity = "legal_entity"
    branch = "branch"
    representative = "representative"
    distributor = "distributor"
    office = "office"
    project_only = "project_only"
    unknown = "unknown"
    not_found = "not_found"

class LeadClass(str, Enum):
    Class_A = "Class_A" # 80-100: Act Now
    Class_B = "Class_B" # 65-79: Research / Nurture
    Class_C = "Class_C" # 45-64: Watch
    Class_D = "Class_D" # 0-44: Reject

class OfferType(str, Enum):
    # Plus UAE Offers
    plusuae_pro_services = "plusuae_pro_services"
    plusuae_business_setup = "plusuae_business_setup"
    plusuae_representation = "plusuae_representation"
    plusuae_project_support = "plusuae_project_support"
    plusuae_registrations_pq = "plusuae_registrations_pq"
    plusuae_oem_support = "plusuae_oem_support"
    # Vortexen Offers
    vortexen_firestopping = "vortexen_firestopping"
    vortexen_fireproofing = "vortexen_fireproofing"
    vortexen_protective_coatings = "vortexen_protective_coatings"
    vortexen_industrial_representation = "vortexen_industrial_representation"
    vortexen_shutdown_support = "vortexen_shutdown_support"

class ChannelType(str, Enum):
    email = "email"
    event_portal = "event_portal"
    linkedin_task = "linkedin_task"
    whatsapp = "whatsapp"
    sms = "sms"
    ai_voice = "ai_voice"

class ReplyClass(str, Enum):
    positive_meeting = "positive_meeting"
    positive_info = "positive_info"
    referral = "referral"
    objection = "objection"
    not_now = "not_now"
    not_interested = "not_interested"
    unsubscribe = "unsubscribe"
    wrong_person = "wrong_person"
    out_of_office = "out_of_office"
    bounce = "bounce"
    legal_privacy = "legal_privacy"
    other = "other"

# Account Models
class AccountBase(BaseModel):
    legal_name: str
    display_name: Optional[str] = None
    domain: str
    hq_country: Optional[str] = "Unknown"
    industry: Optional[str] = "Industrial"
    employee_range: Optional[str] = "50-200"
    uae_presence_type: PresenceType = PresenceType.unknown
    saudi_presence_type: PresenceType = PresenceType.unknown
    presence_evidence: Optional[str] = None

class AccountCreate(AccountBase):
    pass

class AccountResponse(AccountBase):
    id: str
    zoho_crm_id: Optional[str] = None
    created_at: datetime

    model_config = {"from_attributes": True}

# Contact Models
class ContactBase(BaseModel):
    account_id: str
    first_name: str
    last_name: str
    job_title: str
    role_category: str
    work_email: str
    phone_number: Optional[str] = None
    whatsapp_number: Optional[str] = None
    linkedin_url: Optional[str] = None

class ContactResponse(ContactBase):
    id: str
    email_verification_status: str = "verified"
    opt_out_email: bool = False
    opt_out_whatsapp: bool = False
    opt_out_voice: bool = False

# Signal Models
class SignalBase(BaseModel):
    signal_type: str
    source_name: str
    source_url: Optional[str] = None
    account_name: str
    headline: str
    raw_content: str
    extracted_trigger: str
    target_geography: str
    confidence_score: float = Field(..., ge=0.0, le=100.0)

class SignalResponse(SignalBase):
    id: str
    created_at: datetime

# Evidence Brief Model
class EvidenceBrief(BaseModel):
    trigger: str
    company_fact: str
    local_gap: str
    offer_fit: str
    cta: str
    do_not_say: List[str] = ["generic superlatives", "fake familiarity", "we noticed your amazing company", "invented urgency"]

# Opportunity Routing Request & Response
class RouteAccountRequest(BaseModel):
    account_name: str
    domain: str
    hq_country: str
    industry: str
    uae_presence: PresenceType
    saudi_presence: PresenceType
    active_triggers: List[str]
    target_geography: str # 'Abu Dhabi', 'UAE', 'Saudi Arabia'

class ScoreBreakdown(BaseModel):
    service_fit: int # max 25
    buying_intent: int # max 25
    timing: int # max 15
    uae_relevance: int # max 15
    decision_maker: int # max 10
    contactability: int # max 10
    total_score: int

class OpportunityResponse(BaseModel):
    opportunity_id: str
    account_name: str
    domain: str
    company_division: str # 'Plus UAE' or 'Vortexen'
    primary_offer: OfferType
    fallback_offer: OfferType
    target_geography: str
    fit_score: int
    lead_class: LeadClass
    score_breakdown: ScoreBreakdown
    routing_rationale: str
    evidence_brief: EvidenceBrief
    target_roles: List[str]
    next_action: str

# Outreach Copy & Personalization QA
class GenerateOutreachRequest(BaseModel):
    opportunity_id: str
    contact_id: str
    channel: ChannelType = ChannelType.email

class OutreachDraftResponse(BaseModel):
    outreach_id: str
    opportunity_id: str
    contact_id: str
    channel: ChannelType
    recipient_name: str
    recipient_email: str
    subject_line: str
    message_body: str
    evidence_signals: List[str]
    anti_ad_qa_passed: bool
    anti_ad_rejection_reason: Optional[str] = None

# Reply Payload & Handoff
class ProcessReplyRequest(BaseModel):
    outreach_id: str
    contact_email: str
    raw_message: str
    reply_channel: ChannelType = ChannelType.email

class ProcessReplyResponse(BaseModel):
    reply_id: str
    reply_class: ReplyClass
    extracted_intent: str
    sentiment_score: float
    sequence_paused: bool
    handoff_required: bool
    assigned_human_owner: str
    handoff_summary: str
