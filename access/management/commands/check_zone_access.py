from django.core.management.base import BaseCommand, CommandError
from access.models import Card, Zone, ZoneUsage, ZoneAccessLog


class Command(BaseCommand):
    args = '<zone_id> <card_serial_number> <pin_code>'
    help = 'Checks if user with certain access card has access to zone'

    def handle(self, *args, **options):
        if len(args) < 3:
            raise CommandError('Not enough arguments!')

        try:
            zone_id = int(args[0])
            zone = Zone.objects.get(pk=zone_id)
        except (ValueError, Zone.DoesNotExist):
            raise CommandError(
                "Zone should contain numeric primary key of Zone entry.")

        try:
            pin_code = int(args[2])
        except ValueError:
            raise CommandError("Pin code should containe numeric value")

        try:
            card_number = int(args[1], 16)
        except ValueError:
            raise CommandError(
                "Card number should contain hexadecimal number.")

        access_log = ZoneAccessLog.objects.create(
            serial_number=card_number, zone=zone, pin_code=pin_code,
            access_granted=False)

        # get corresponding card entry
        try:
            card = Card.objects.get(serial_number=card_number,
                                    pin_code=pin_code, is_active=True,
                                    is_deleted=False)
        except Card.DoesNotExist:
            raise CommandError("Card does not exist or wrong pin code.")

        # check if user has access to this zone
        if len(card.user.zone_access_set.filter(zone=zone)) > 0 and \
           card.user.is_active:
                access_log.access_granted = True
                access_log.save()
                ZoneUsage.objects.create(card=card, zone=zone)
                self.stdout.write("Access granted.")
        else:
            raise CommandError("Access denied.")
