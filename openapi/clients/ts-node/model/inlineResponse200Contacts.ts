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

export class InlineResponse200Contacts {
    /**
    * The type of contact
    */
    'type'?: string;
    /**
    * Human readable label of the contact
    */
    'label'?: string;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "type",
            "baseName": "type",
            "type": "string"
        },
        {
            "name": "label",
            "baseName": "label",
            "type": "string"
        }    ];

    static getAttributeTypeMap() {
        return InlineResponse200Contacts.attributeTypeMap;
    }
}

