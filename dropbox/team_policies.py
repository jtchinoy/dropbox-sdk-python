# -*- coding: utf-8 -*-
# Auto-generated by BabelAPI, do not modify.
try:
    from . import babel_validators as bv
except (SystemError, ValueError):
    # Catch errors raised when importing a relative module when not in a package.
    # This makes testing this file directly (outside of a package) easier.
    import babel_validators as bv

class EmmState(object):
    """
    This class acts as a tagged union. Only one of the ``is_*`` methods will
    return true. To get the associated value of a tag (if one exists), use the
    corresponding ``get_*`` method.

    :ivar disabled: Emm token is disabled
    :ivar optional: Emm token is optional
    :ivar required: Emm token is required
    """

    __slots__ = ['_tag', '_value']

    _catch_all = 'other'
    # Attribute is overwritten below the class definition
    disabled = None
    # Attribute is overwritten below the class definition
    optional = None
    # Attribute is overwritten below the class definition
    required = None
    # Attribute is overwritten below the class definition
    other = None

    def __init__(self, tag, value=None):
        assert tag in self._tagmap, 'Invalid tag %r.' % tag
        validator = self._tagmap[tag]
        if isinstance(validator, bv.Void):
            assert value is None, 'Void type union member must have None value.'
        elif isinstance(validator, (bv.Struct, bv.Union)):
            validator.validate_type_only(value)
        else:
            validator.validate(value)
        self._tag = tag
        self._value = value

    def is_disabled(self):
        """
        Check if the union tag is ``disabled``.

        :rtype: bool
        """
        return self._tag == 'disabled'

    def is_optional(self):
        """
        Check if the union tag is ``optional``.

        :rtype: bool
        """
        return self._tag == 'optional'

    def is_required(self):
        """
        Check if the union tag is ``required``.

        :rtype: bool
        """
        return self._tag == 'required'

    def is_other(self):
        """
        Check if the union tag is ``other``.

        :rtype: bool
        """
        return self._tag == 'other'

    def __repr__(self):
        return 'EmmState(%r, %r)' % (self._tag, self._value)

class SharedFolderJoinPolicy(object):
    """
    Policy governing which shared folders a team member can join.

    This class acts as a tagged union. Only one of the ``is_*`` methods will
    return true. To get the associated value of a tag (if one exists), use the
    corresponding ``get_*`` method.

    :ivar from_team_only: Team members can only join folders shared by
        teammates.
    :ivar from_anyone: Team members can join any shared folder, including those
        shared by users outside the team.
    """

    __slots__ = ['_tag', '_value']

    _catch_all = 'other'
    # Attribute is overwritten below the class definition
    from_team_only = None
    # Attribute is overwritten below the class definition
    from_anyone = None
    # Attribute is overwritten below the class definition
    other = None

    def __init__(self, tag, value=None):
        assert tag in self._tagmap, 'Invalid tag %r.' % tag
        validator = self._tagmap[tag]
        if isinstance(validator, bv.Void):
            assert value is None, 'Void type union member must have None value.'
        elif isinstance(validator, (bv.Struct, bv.Union)):
            validator.validate_type_only(value)
        else:
            validator.validate(value)
        self._tag = tag
        self._value = value

    def is_from_team_only(self):
        """
        Check if the union tag is ``from_team_only``.

        :rtype: bool
        """
        return self._tag == 'from_team_only'

    def is_from_anyone(self):
        """
        Check if the union tag is ``from_anyone``.

        :rtype: bool
        """
        return self._tag == 'from_anyone'

    def is_other(self):
        """
        Check if the union tag is ``other``.

        :rtype: bool
        """
        return self._tag == 'other'

    def __repr__(self):
        return 'SharedFolderJoinPolicy(%r, %r)' % (self._tag, self._value)

class SharedFolderMemberPolicy(object):
    """
    Policy governing who can be a member of a folder shared by a team member.

    This class acts as a tagged union. Only one of the ``is_*`` methods will
    return true. To get the associated value of a tag (if one exists), use the
    corresponding ``get_*`` method.

    :ivar team: Only a teammate can be a member of a folder shared by a team
        member.
    :ivar anyone: Anyone can be a member of a folder shared by a team member.
    """

    __slots__ = ['_tag', '_value']

    _catch_all = 'other'
    # Attribute is overwritten below the class definition
    team = None
    # Attribute is overwritten below the class definition
    anyone = None
    # Attribute is overwritten below the class definition
    other = None

    def __init__(self, tag, value=None):
        assert tag in self._tagmap, 'Invalid tag %r.' % tag
        validator = self._tagmap[tag]
        if isinstance(validator, bv.Void):
            assert value is None, 'Void type union member must have None value.'
        elif isinstance(validator, (bv.Struct, bv.Union)):
            validator.validate_type_only(value)
        else:
            validator.validate(value)
        self._tag = tag
        self._value = value

    def is_team(self):
        """
        Check if the union tag is ``team``.

        :rtype: bool
        """
        return self._tag == 'team'

    def is_anyone(self):
        """
        Check if the union tag is ``anyone``.

        :rtype: bool
        """
        return self._tag == 'anyone'

    def is_other(self):
        """
        Check if the union tag is ``other``.

        :rtype: bool
        """
        return self._tag == 'other'

    def __repr__(self):
        return 'SharedFolderMemberPolicy(%r, %r)' % (self._tag, self._value)

class SharedLinkCreatePolicy(object):
    """
    Policy governing the visibility of newly created shared links.

    This class acts as a tagged union. Only one of the ``is_*`` methods will
    return true. To get the associated value of a tag (if one exists), use the
    corresponding ``get_*`` method.

    :ivar default_public: By default, anyone can access newly created shared
        links. No login will be required to access the shared links unless
        overridden.
    :ivar default_team_only: By default, only members of the same team can
        access newly created shared links. Login will be required to access the
        shared links unless overridden.
    :ivar team_only: Only members of the same team can access newly created
        shared links. Login will be required to access the shared links.
    """

    __slots__ = ['_tag', '_value']

    _catch_all = 'other'
    # Attribute is overwritten below the class definition
    default_public = None
    # Attribute is overwritten below the class definition
    default_team_only = None
    # Attribute is overwritten below the class definition
    team_only = None
    # Attribute is overwritten below the class definition
    other = None

    def __init__(self, tag, value=None):
        assert tag in self._tagmap, 'Invalid tag %r.' % tag
        validator = self._tagmap[tag]
        if isinstance(validator, bv.Void):
            assert value is None, 'Void type union member must have None value.'
        elif isinstance(validator, (bv.Struct, bv.Union)):
            validator.validate_type_only(value)
        else:
            validator.validate(value)
        self._tag = tag
        self._value = value

    def is_default_public(self):
        """
        Check if the union tag is ``default_public``.

        :rtype: bool
        """
        return self._tag == 'default_public'

    def is_default_team_only(self):
        """
        Check if the union tag is ``default_team_only``.

        :rtype: bool
        """
        return self._tag == 'default_team_only'

    def is_team_only(self):
        """
        Check if the union tag is ``team_only``.

        :rtype: bool
        """
        return self._tag == 'team_only'

    def is_other(self):
        """
        Check if the union tag is ``other``.

        :rtype: bool
        """
        return self._tag == 'other'

    def __repr__(self):
        return 'SharedLinkCreatePolicy(%r, %r)' % (self._tag, self._value)

class TeamPolicies(object):
    """
    Policies governing team members.

    :ivar sharing: Policies governing sharing.
    :ivar emm_state: This describes the Enterprise Mobility Management (EMM)
        state for this team. This information can be used to understand if an
        organization is integrating with a third-party EMM vendor to further
        manage and apply restrictions upon the team's Dropbox usage on mobile
        devices. This is a new feature and in the future we'll be adding more
        new fields and additional documentation.
    """

    __slots__ = [
        '_sharing_value',
        '_sharing_present',
        '_emm_state_value',
        '_emm_state_present',
    ]

    _has_required_fields = True

    def __init__(self,
                 sharing=None,
                 emm_state=None):
        self._sharing_value = None
        self._sharing_present = False
        self._emm_state_value = None
        self._emm_state_present = False
        if sharing is not None:
            self.sharing = sharing
        if emm_state is not None:
            self.emm_state = emm_state

    @property
    def sharing(self):
        """
        Policies governing sharing.

        :rtype: TeamSharingPolicies
        """
        if self._sharing_present:
            return self._sharing_value
        else:
            raise AttributeError("missing required field 'sharing'")

    @sharing.setter
    def sharing(self, val):
        self._sharing_validator.validate_type_only(val)
        self._sharing_value = val
        self._sharing_present = True

    @sharing.deleter
    def sharing(self):
        self._sharing_value = None
        self._sharing_present = False

    @property
    def emm_state(self):
        """
        This describes the Enterprise Mobility Management (EMM) state for this
        team. This information can be used to understand if an organization is
        integrating with a third-party EMM vendor to further manage and apply
        restrictions upon the team's Dropbox usage on mobile devices. This is a
        new feature and in the future we'll be adding more new fields and
        additional documentation.

        :rtype: EmmState
        """
        if self._emm_state_present:
            return self._emm_state_value
        else:
            raise AttributeError("missing required field 'emm_state'")

    @emm_state.setter
    def emm_state(self, val):
        self._emm_state_validator.validate_type_only(val)
        self._emm_state_value = val
        self._emm_state_present = True

    @emm_state.deleter
    def emm_state(self):
        self._emm_state_value = None
        self._emm_state_present = False

    def __repr__(self):
        return 'TeamPolicies(sharing={!r}, emm_state={!r})'.format(
            self._sharing_value,
            self._emm_state_value,
        )

class TeamSharingPolicies(object):
    """
    Policies governing sharing within and outside of the team.

    :ivar shared_folder_member_policy: Who can join folders shared by team
        members.
    :ivar shared_folder_join_policy: Which shared folders team members can join.
    :ivar shared_link_create_policy: What is the visibility of newly created
        shared links.
    """

    __slots__ = [
        '_shared_folder_member_policy_value',
        '_shared_folder_member_policy_present',
        '_shared_folder_join_policy_value',
        '_shared_folder_join_policy_present',
        '_shared_link_create_policy_value',
        '_shared_link_create_policy_present',
    ]

    _has_required_fields = True

    def __init__(self,
                 shared_folder_member_policy=None,
                 shared_folder_join_policy=None,
                 shared_link_create_policy=None):
        self._shared_folder_member_policy_value = None
        self._shared_folder_member_policy_present = False
        self._shared_folder_join_policy_value = None
        self._shared_folder_join_policy_present = False
        self._shared_link_create_policy_value = None
        self._shared_link_create_policy_present = False
        if shared_folder_member_policy is not None:
            self.shared_folder_member_policy = shared_folder_member_policy
        if shared_folder_join_policy is not None:
            self.shared_folder_join_policy = shared_folder_join_policy
        if shared_link_create_policy is not None:
            self.shared_link_create_policy = shared_link_create_policy

    @property
    def shared_folder_member_policy(self):
        """
        Who can join folders shared by team members.

        :rtype: SharedFolderMemberPolicy
        """
        if self._shared_folder_member_policy_present:
            return self._shared_folder_member_policy_value
        else:
            raise AttributeError("missing required field 'shared_folder_member_policy'")

    @shared_folder_member_policy.setter
    def shared_folder_member_policy(self, val):
        self._shared_folder_member_policy_validator.validate_type_only(val)
        self._shared_folder_member_policy_value = val
        self._shared_folder_member_policy_present = True

    @shared_folder_member_policy.deleter
    def shared_folder_member_policy(self):
        self._shared_folder_member_policy_value = None
        self._shared_folder_member_policy_present = False

    @property
    def shared_folder_join_policy(self):
        """
        Which shared folders team members can join.

        :rtype: SharedFolderJoinPolicy
        """
        if self._shared_folder_join_policy_present:
            return self._shared_folder_join_policy_value
        else:
            raise AttributeError("missing required field 'shared_folder_join_policy'")

    @shared_folder_join_policy.setter
    def shared_folder_join_policy(self, val):
        self._shared_folder_join_policy_validator.validate_type_only(val)
        self._shared_folder_join_policy_value = val
        self._shared_folder_join_policy_present = True

    @shared_folder_join_policy.deleter
    def shared_folder_join_policy(self):
        self._shared_folder_join_policy_value = None
        self._shared_folder_join_policy_present = False

    @property
    def shared_link_create_policy(self):
        """
        What is the visibility of newly created shared links.

        :rtype: SharedLinkCreatePolicy
        """
        if self._shared_link_create_policy_present:
            return self._shared_link_create_policy_value
        else:
            raise AttributeError("missing required field 'shared_link_create_policy'")

    @shared_link_create_policy.setter
    def shared_link_create_policy(self, val):
        self._shared_link_create_policy_validator.validate_type_only(val)
        self._shared_link_create_policy_value = val
        self._shared_link_create_policy_present = True

    @shared_link_create_policy.deleter
    def shared_link_create_policy(self):
        self._shared_link_create_policy_value = None
        self._shared_link_create_policy_present = False

    def __repr__(self):
        return 'TeamSharingPolicies(shared_folder_member_policy={!r}, shared_folder_join_policy={!r}, shared_link_create_policy={!r})'.format(
            self._shared_folder_member_policy_value,
            self._shared_folder_join_policy_value,
            self._shared_link_create_policy_value,
        )

EmmState._disabled_validator = bv.Void()
EmmState._optional_validator = bv.Void()
EmmState._required_validator = bv.Void()
EmmState._other_validator = bv.Void()
EmmState._tagmap = {
    'disabled': EmmState._disabled_validator,
    'optional': EmmState._optional_validator,
    'required': EmmState._required_validator,
    'other': EmmState._other_validator,
}

EmmState.disabled = EmmState('disabled')
EmmState.optional = EmmState('optional')
EmmState.required = EmmState('required')
EmmState.other = EmmState('other')

SharedFolderJoinPolicy._from_team_only_validator = bv.Void()
SharedFolderJoinPolicy._from_anyone_validator = bv.Void()
SharedFolderJoinPolicy._other_validator = bv.Void()
SharedFolderJoinPolicy._tagmap = {
    'from_team_only': SharedFolderJoinPolicy._from_team_only_validator,
    'from_anyone': SharedFolderJoinPolicy._from_anyone_validator,
    'other': SharedFolderJoinPolicy._other_validator,
}

SharedFolderJoinPolicy.from_team_only = SharedFolderJoinPolicy('from_team_only')
SharedFolderJoinPolicy.from_anyone = SharedFolderJoinPolicy('from_anyone')
SharedFolderJoinPolicy.other = SharedFolderJoinPolicy('other')

SharedFolderMemberPolicy._team_validator = bv.Void()
SharedFolderMemberPolicy._anyone_validator = bv.Void()
SharedFolderMemberPolicy._other_validator = bv.Void()
SharedFolderMemberPolicy._tagmap = {
    'team': SharedFolderMemberPolicy._team_validator,
    'anyone': SharedFolderMemberPolicy._anyone_validator,
    'other': SharedFolderMemberPolicy._other_validator,
}

SharedFolderMemberPolicy.team = SharedFolderMemberPolicy('team')
SharedFolderMemberPolicy.anyone = SharedFolderMemberPolicy('anyone')
SharedFolderMemberPolicy.other = SharedFolderMemberPolicy('other')

SharedLinkCreatePolicy._default_public_validator = bv.Void()
SharedLinkCreatePolicy._default_team_only_validator = bv.Void()
SharedLinkCreatePolicy._team_only_validator = bv.Void()
SharedLinkCreatePolicy._other_validator = bv.Void()
SharedLinkCreatePolicy._tagmap = {
    'default_public': SharedLinkCreatePolicy._default_public_validator,
    'default_team_only': SharedLinkCreatePolicy._default_team_only_validator,
    'team_only': SharedLinkCreatePolicy._team_only_validator,
    'other': SharedLinkCreatePolicy._other_validator,
}

SharedLinkCreatePolicy.default_public = SharedLinkCreatePolicy('default_public')
SharedLinkCreatePolicy.default_team_only = SharedLinkCreatePolicy('default_team_only')
SharedLinkCreatePolicy.team_only = SharedLinkCreatePolicy('team_only')
SharedLinkCreatePolicy.other = SharedLinkCreatePolicy('other')

TeamPolicies._sharing_validator = bv.Struct(TeamSharingPolicies)
TeamPolicies._emm_state_validator = bv.Union(EmmState)
TeamPolicies._all_field_names_ = set([
    'sharing',
    'emm_state',
])
TeamPolicies._all_fields_ = [
    ('sharing', TeamPolicies._sharing_validator),
    ('emm_state', TeamPolicies._emm_state_validator),
]

TeamSharingPolicies._shared_folder_member_policy_validator = bv.Union(SharedFolderMemberPolicy)
TeamSharingPolicies._shared_folder_join_policy_validator = bv.Union(SharedFolderJoinPolicy)
TeamSharingPolicies._shared_link_create_policy_validator = bv.Union(SharedLinkCreatePolicy)
TeamSharingPolicies._all_field_names_ = set([
    'shared_folder_member_policy',
    'shared_folder_join_policy',
    'shared_link_create_policy',
])
TeamSharingPolicies._all_fields_ = [
    ('shared_folder_member_policy', TeamSharingPolicies._shared_folder_member_policy_validator),
    ('shared_folder_join_policy', TeamSharingPolicies._shared_folder_join_policy_validator),
    ('shared_link_create_policy', TeamSharingPolicies._shared_link_create_policy_validator),
]
