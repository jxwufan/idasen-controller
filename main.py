#!/usr/bin/python3

import argparse
import desk
import logging
import asyncio

def get_parser():
    parser = argparse.ArgumentParser(description='Idasen Desk Controller')
    parser.add_argument('--address', type=str, default='01CE3D4D-9CF3-44B8-83B8-31CE5333EF17')
    parser.add_argument('--verbose', action='store_true')
    parser.add_argument('--position', type=str)
    return parser


async def main():
    parser = get_parser()
    args = parser.parse_args()
    print(args)
    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.INFO)
    bt_desk = desk.IdasenDesk("C7:A8:48:D5:E9:0E")
    if not await bt_desk._connect_and_validate():
        return 
    print(args.position)
    if args.position == "stand":
        await bt_desk.move_to(5200)
    else:
        await bt_desk.move_to(1200)

    await bt_desk._disconnect()

if __name__ == '__main__':
    asyncio.run(main())