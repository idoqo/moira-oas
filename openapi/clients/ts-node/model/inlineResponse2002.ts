/**
 * Moira Alert
 * This is an API description for [Moira Alert project](https://moira.readthedocs.io/en/latest/overview.html). Please check <https://github.com/moira-alert/>
 *
 * The version of the OpenAPI document: 2.5.1.48
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { RequestFile } from '../api';
import { Event } from './event';

export class InlineResponse2002 {
    /**
    * Current page being displayed. Pages are zero-indexed.
    */
    'page'?: number;
    /**
    * Maximum number of items displayed per page.
    */
    'size'?: number;
    /**
    * Total number of available events for the trigger
    */
    'total'?: number;
    /**
    * List of trigger events
    */
    'list'?: Array<Event>;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "page",
            "baseName": "page",
            "type": "number"
        },
        {
            "name": "size",
            "baseName": "size",
            "type": "number"
        },
        {
            "name": "total",
            "baseName": "total",
            "type": "number"
        },
        {
            "name": "list",
            "baseName": "list",
            "type": "Array<Event>"
        }    ];

    static getAttributeTypeMap() {
        return InlineResponse2002.attributeTypeMap;
    }
}
